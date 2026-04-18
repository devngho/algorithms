import java.util.Scanner
import java.util.Stack

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val valid = listOf('(', ')', '[', ']')
    val map = mapOf(')' to '(', ']' to '[')

    case@ while (true) {
        val str = nextLine()
        if (str == ".") break

        val stack = Stack<Char>()

        for (it in str.filter { it in valid }) {
            if (it in map.keys) {
                if (stack.isNotEmpty() && stack.last() == map[it]) stack.pop()
                else {
                    appendLine("no")
                    continue@case
                }
            } else stack.push(it)
        }

        if (stack.isEmpty()) appendLine("yes") else appendLine("no")
    }
}.let { print(it) } }