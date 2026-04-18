import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    nextLine()
    val str = nextLine()

    val hash = str.map { it.code - 'a'.code + 1 }.mapIndexed { i, v -> v.toBigInteger() * (31.toBigInteger().pow(i)) }.sumOf { it } % 1234567891.toBigInteger()

    appendLine(hash)
}.let { print(it) } }