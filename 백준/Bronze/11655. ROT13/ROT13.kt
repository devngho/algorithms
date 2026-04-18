// random marathon 5
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val s = nextLine()

    val upper = ('A'..'Z').toList()
    val lower = ('a'..'z').toList()

    s.map { c ->
        if ('A' <= c && c <= 'Z') upper[(upper.indexOf(c) + 13) % 26]
        else if ('a' <= c && c <= 'z') lower[(lower.indexOf(c) + 13) % 26]
        else c
    }.forEach { append(it) }
}.let { println(it) } }