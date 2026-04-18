import java.util.Scanner
import kotlin.collections.forEach
import kotlin.math.max
import kotlin.math.min

val opBinding = mapOf(
    Token.EndOfLine to -1,
    Token.Plus to 2,
    Token.Minus to 2,
    Token.Asterisk to 3,
    Token.Slash to 4,
    Token.Colon to 1,
    Token.Equal to 0
)
val unaryOperatorsBinding = mapOf(
    Token.Print to 0,
    Token.Plus to 5,
    Token.Minus to 5,
    Token.Asterisk to 5,
    Token.Slash to 5,
)
data class Lexer(val tokens: List<Token>, var cursor: Int)

sealed interface Statement {
    data class AssignStatement(val ref: Value.ListRef, val value: Expr): Statement

    data class PrintStatement(val value: Expr): Statement
}

sealed interface Token {
    data class StringToken(val value: String): Token
    data class IntToken(val value: Int): Token
    data object Print: Token
    data object LParen: Token
    data object LBracket: Token
    data object RParen: Token
    data object RBracket: Token
    data object Plus: Token
    data object Asterisk: Token
    data object Minus: Token
    data object Slash: Token
    data object Colon: Token
    data object EndOfLine: Token
    data object Equal: Token
}

val operators = mapOf(
    '(' to Token.LParen,
    ')' to Token.RParen,
    '[' to Token.LBracket,
    ']' to Token.RBracket,
    '+' to Token.Plus,
    '-' to Token.Minus,
    '*' to Token.Asterisk,
    '/' to Token.Slash,
    ':' to Token.Colon,
    '=' to Token.Equal,
    ' ' to null,
    '\n' to Token.EndOfLine,
)

fun tokenize(text: String): List<Token> {
    val res = mutableListOf<Token>()
    var cursor = 0

    while (cursor < text.count()) {
        if (text[cursor].isDigit()) {
            var tmp = 0

            while (cursor < text.count() && text[cursor].isDigit()) {
                tmp = 10 * tmp + text[cursor].digitToInt()
                cursor++
            }

            res.add(Token.IntToken(tmp))
        } else if (operators.containsKey(text[cursor])) {
            operators[text[cursor]]?.let { res.add(it) }
            cursor++
        } else {
            res.add(buildString {
                while (cursor < text.count() && !text[cursor].isDigit() && !operators.containsKey(text[cursor])) {
                    append(text[cursor])
                    cursor++
                }
            }.let {
                if (it == "print") Token.Print
                else Token.StringToken(it)
            })
        }
    }

    return res.toList()
}

data class Env(
    val refs: MutableMap<Value.ListRef, Value> = mutableMapOf<Value.ListRef, Value>()
)

sealed interface Expr {
    data class SliceExpr(val value: Expr, val begin: Int, val end: Int): Expr {
        override fun execute(env: Env): Value {
            val value = this.value.execute(env).asLazyList(env)

            return if (value?.count != null) { // finite
                Value.ListValue({
                    if (end != -1 && it+begin >= end) return@ListValue value.get(end-1)

                    value.get(it+begin)
                }, max(0, min(if (end != -1) end-begin else Int.MAX_VALUE, value.count-begin)))
            } else {
                Value.ListValue({
                    val v = this.value.execute(env).asLazyList(env)!!

                    if (end != -1 && it+begin >= end) return@ListValue v.get(end-1)

                    v.get(it+begin)
                }, if (end != -1) ( if (begin >= end) 0 else end-begin ) else null)
            }
        }


        override fun toString(): String = "($value)[$begin:$end]"
    }

    data class UnaryOp(val op: Token, val value: Expr): Expr {
        override fun execute(env: Env): Value {
            val list = value.execute(env).asEagerList(env)

            return when (op) {
                Token.Plus -> list.fold(0) { acc, value -> value.asInt(env) + acc }
                Token.Minus -> {
                    var v = list[0].asInt(env)
                    list.drop(1).forEach { v -= it.asInt(env) }
                    v
                }
                Token.Asterisk -> list.fold(1) { acc, value -> value.asInt(env) * acc }
                Token.Slash -> {
                    var v = list[0].asInt(env)
                    list.drop(1).forEach { v /= it.asInt(env) }
                    v
                }
                else -> throw IllegalStateException()
            }.let { Value.IntValue(it) }
        }

        override fun toString(): String = "${op}(${value})"
    }

    data class BinaryOp(val left: Expr, val op: Token, val right: Expr): Expr {
        override fun execute(env: Env): Value {
            if (op == Token.Colon) {
                val l = left.execute(env).asLazyList(env)!!

                if (l.count == null) return l // l is infinite

                val left = l.asEagerList(env)

                return Value.ListValue({
                    if (it < left.count()) return@ListValue left[it]

                    right.execute(env).asLazyList(env)!!.get(it-left.count())
                }, right.execute(env).asLazyList(env)?.count?.let { it + left.count() })
            }

            val leftList = left.execute(env).asLazyList(env)
            val rightList = right.execute(env).asLazyList(env)

            if (leftList?.count == 0 || rightList?.count == 0) return Value.ListValue({ Value.Unit }, 0)

            val count = if (leftList?.count == null || rightList?.count == null) null else (max(leftList.count, rightList.count))

            return when (op) {
                Token.Plus -> Value.ListValue({
                    Value.IntValue(left.execute(env).asLazyList(env)!!.get(it).asInt(env) + right.execute(env).asLazyList(env)!!.get(it).asInt(env))
                }, count)
                Token.Minus -> Value.ListValue({
                    Value.IntValue(left.execute(env).asLazyList(env)!!.get(it).asInt(env) - right.execute(env).asLazyList(env)!!.get(it).asInt(env))
                }, count)
                Token.Asterisk -> Value.ListValue({
                    Value.IntValue(left.execute(env).asLazyList(env)!!.get(it).asInt(env) * right.execute(env).asLazyList(env)!!.get(it).asInt(env))
                }, count)
                Token.Slash -> Value.ListValue({
                    Value.IntValue(left.execute(env).asLazyList(env)!!.get(it).asInt(env) / right.execute(env).asLazyList(env)!!.get(it).asInt(env))
                }, count)
                else -> throw IllegalStateException("$op")
            }
        }

        override fun toString(): String = "($left) $op ($right)"
    }

    data class StringLiteral(val value: String): Expr {
        override fun execute(env: Env): Value {
            return Value.ListRef(this.value)
        }

        override fun toString(): String = value
    }

    data class IntLiteral(val value: Int): Expr {
        override fun execute(env: Env): Value = Value.IntValue(this.value)

        override fun toString(): String = value.toString()
    }

    fun execute(env: Env): Value
}

sealed interface Value {
    @JvmInline
    value class ListRef(val name: String): Value

    data class ListValue(val get: (Int) -> Value, val count: Int?): Value {
        override fun toString(): String = if (count != null) (0 until count).map { get(it) }.joinToString(":") else "?"
    }

    @JvmInline
    value class IntValue(val value: Int): Value {
        override fun toString(): String = value.toString()
    }

    data object Unit: Value

    fun asInt(env: Env): Int = when(this) {
        is ListRef -> env.refs[this]!!.asInt(env)
        is ListValue -> if (this.count == 1) this.get(0).asInt(env) else throw IllegalStateException()
        is IntValue -> this.value
        else -> throw IllegalStateException()
    }

    fun asLazyList(env: Env): Value.ListValue? = when(this) {
        is ListRef -> env.refs[this]?.asLazyList(env)
        is ListValue -> this
        is IntValue -> ListValue({ this }, 1)
        else -> throw IllegalStateException()
    }

    fun asEagerList(env: Env): List<Value> = when(this) {
        is ListRef -> env.refs[this]!!.asEagerList(env)
        is ListValue -> (0 until this.count!!).map { get(it) }
        is IntValue -> listOf(this)
        else -> throw IllegalStateException()
    }
}

fun pratt(lexer: Lexer, minBp: Int = 0): Expr {
    var left: Expr = when (lexer.tokens[lexer.cursor]) {
        Token.LParen -> {
            lexer.cursor++
            pratt(lexer, 0).also { lexer.cursor++ }
        }
        is Token.StringToken -> Expr.StringLiteral((lexer.tokens[lexer.cursor] as Token.StringToken).value).also { lexer.cursor++ }
        is Token.IntToken -> Expr.IntLiteral((lexer.tokens[lexer.cursor] as Token.IntToken).value).also { lexer.cursor++ }
        in unaryOperatorsBinding -> {
            val op = lexer.tokens[lexer.cursor]
            lexer.cursor++
            Expr.UnaryOp(op, pratt(lexer, unaryOperatorsBinding[op]!!))
        }
        else -> throw IllegalArgumentException("no ${lexer.tokens[lexer.cursor]}")
    }

    while (lexer.cursor < lexer.tokens.count() - 1) {
        val op = lexer.tokens[lexer.cursor]

        when (op) {
            Token.LParen -> {
                lexer.cursor++
                val right = pratt(lexer, 0)
                lexer.cursor++
                left = Expr.BinaryOp(left, op, right)
            }
            Token.LBracket -> {
                lexer.cursor++

                val begin = if (lexer.tokens[lexer.cursor] == Token.Colon) 0 else {
                    (lexer.tokens[lexer.cursor] as Token.IntToken).value.also { lexer.cursor++ }
                }

                lexer.cursor++

                val end = if (lexer.tokens[lexer.cursor] == Token.RBracket) -1 else {
                    (lexer.tokens[lexer.cursor] as Token.IntToken).value.also { lexer.cursor++ }
                }

                lexer.cursor++

                left = Expr.SliceExpr(left, begin, end)
            }
            Token.RParen -> {
                break
            }
            else -> {
                if (!opBinding.containsKey(op)) println("sibal: $op")
                val bp = opBinding[op]!!

                if (bp <= minBp) break
                lexer.cursor++
                val right = pratt(lexer, bp)
                left = Expr.BinaryOp(left, op, right)
            }
        }
    }

    return left
}

fun parseStatement(value: List<Expr>): Statement = when(value[0]) {
    is Expr.UnaryOp -> {
        if ((value[0] as Expr.UnaryOp).op is Token.Print) {
            Statement.PrintStatement((value[0] as Expr.UnaryOp).value)
        } else throw IllegalArgumentException("$value")
    }
    else -> throw IllegalArgumentException("${value[0]}")
}

fun parse(lexer: Lexer): List<Statement> {
    val statements = mutableListOf<Statement>()
    val expressions = mutableListOf<Expr>()

    while (lexer.cursor < lexer.tokens.count()) {
        expressions.add(pratt(lexer))

        when (lexer.tokens[lexer.cursor]) {
            is Token.Equal -> {
                val left = expressions[0]
                lexer.cursor++
                statements.add(Statement.AssignStatement(Value.ListRef((left as Expr.StringLiteral).value), pratt(lexer)))
                lexer.cursor++
                expressions.clear()
            }
            is Token.EndOfLine -> {
                statements.add(parseStatement(expressions))
                expressions.clear()
                lexer.cursor++
            }
            else -> {}
        }
    }

    return statements
}

fun main() = with(Scanner(System.`in`.bufferedReader()))  {
    val op = buildString {
        while (true) {
            val value = nextLine()
            if (value == "#") break

            appendLine(value)
        }
    }

    val env = Env()

    parse(Lexer(tokenize(op), 0)).forEach {
        when(it) {
            is Statement.PrintStatement -> {
                println(it.value.execute(env).let { v ->
                    if (v is Value.ListRef) v.asLazyList(env)
                    else v
                })
            }

            is Statement.AssignStatement -> {
                env.refs[it.ref] = it.value.execute(env)
            }
        }
    }
}
