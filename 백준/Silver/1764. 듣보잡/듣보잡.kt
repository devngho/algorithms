import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val (n, m) = nextInt() to nextInt()

    nextLine()
    val notHeard = List(n) { nextLine() }.toSet()
    val notSeen = List(m) { nextLine() }.toSet()

    val intersection = notHeard.intersect(notSeen)

    appendLine(intersection.count())
    intersection.sorted().forEach {
        appendLine(it)
    }
}.let { print(it) } }