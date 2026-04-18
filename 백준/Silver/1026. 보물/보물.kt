import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val a = List(n) { nextInt() }.sorted()
    val b = List(n) { nextInt() }.sorted()

    println(List(n) { a[n-it-1] * b[it] }.sum())
}.let { print(it) } }