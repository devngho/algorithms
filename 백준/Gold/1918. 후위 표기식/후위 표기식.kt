package io.github.devngho.algorthmkt

import java.util.Scanner

val opBinding = mapOf('+' to 1, '-' to 1, '*' to 2, '/' to 2)
data class Lexer(val text: String, var cursor: Int)

sealed interface Expr {
    data class Op(val left: Expr, val op: Char, val right: Expr): Expr {
        override fun toPostfix(): String = "${left.toPostfix()}${right.toPostfix()}$op"
    }
    data class Literal(val value: Char): Expr {
        override fun toPostfix(): String = "$value"
    }

    fun toPostfix(): String
}

fun pratt(lexer: Lexer, minBp: Int = 0): Expr {
    var left: Expr = if (lexer.text[lexer.cursor] == '(') {
        lexer.cursor++
        pratt(lexer, 0)
    } else { Expr.Literal(lexer.text[lexer.cursor]) }
    lexer.cursor++

    while (lexer.cursor < lexer.text.count() - 1) {
        val op = lexer.text[lexer.cursor]

        if (op == '(') {
            lexer.cursor++
            val right = pratt(lexer, 0)
            lexer.cursor++
            left = Expr.Op(left, op, right)
        } else if (op == ')') {
            break
        } else {
            val bp = opBinding[op]!!

            if (bp <= minBp) break
            lexer.cursor++
            val right = pratt(lexer, bp)
            left = Expr.Op(left, op, right)
        }
    }

    return left
}

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val op = nextLine()
    appendLine(pratt(Lexer(op, 0)).toPostfix())
}.let { print(it) } }