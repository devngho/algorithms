import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    repeat(nextInt()) {
        val gears = mutableMapOf<String, Int>()
        repeat(nextInt().also { nextLine() }) {
            val (_, kind) = nextLine().split(" ")
            gears[kind] = (gears[kind] ?: 0) + 1
        }
        appendLine(gears.toList().fold(1) { acc, pair -> acc * (pair.second + 1) } - 1)
    }
}.let { print(it) } }