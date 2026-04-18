import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val coords = List(nextInt()) { nextInt() }
    val map = coords.distinct().sorted().mapIndexed { index, i -> index to i }.associate { it.second to it.first }
    appendLine(coords.joinToString(" ") { map[it].toString() })
}.let { print(it) } }