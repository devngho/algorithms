import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val time = MutableList(nextInt()) { nextInt() }.sorted()

    var sum = 0
    var duration = 0
    time.forEach {
        sum += duration + it
        duration += it
    }

    appendLine(sum)
}.let { print(it) } }