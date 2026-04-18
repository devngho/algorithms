import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()

    for (i in 1 until n) {
        val digitsSum = i.toString().toList().sumOf { it.digitToInt() }
        val destructedSum = i + digitsSum

        if (destructedSum == n) {
            appendLine(i)
            return@buildString
        }
    }

    appendLine("0")
}.let { print(it) } }