import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val numbers = List(n) { nextInt() }
    val m = nextInt()
    val prefix = numbers.scan(0) { acc, it -> acc + it }

    repeat(m) {
        val (i, j) = nextInt() to nextInt()

        appendLine(prefix[j] - prefix[i-1])
    }
}.let { print(it) } }