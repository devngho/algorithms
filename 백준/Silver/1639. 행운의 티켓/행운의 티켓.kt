// random marathon 8
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val s = nextLine()
    var maxLength = 0

    (0 until s.count()).forEach { left ->
        (left + 1 until s.count() step 2).forEach { right ->
            val len = right - left + 1
            val n = len / 2

            if (maxLength < len && s.substring((left until (left + n))).sumOf { it.digitToInt() } == s.substring(((left + n)..right)).sumOf { it.digitToInt() })
                maxLength = len
        }
    }

    appendLine(maxLength)
}.let { print(it) } }