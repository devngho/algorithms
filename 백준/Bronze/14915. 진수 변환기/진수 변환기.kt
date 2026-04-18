// random marathon 3
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val m = nextInt()
    val n = nextInt()

    appendLine(m.toString(n).uppercase())
}.let { print(it) } }