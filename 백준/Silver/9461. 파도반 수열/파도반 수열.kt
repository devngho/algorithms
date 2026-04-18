import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val arr = mutableListOf<Long>(0, 0, 0, 1, 1, 1)

    (5..105).forEach {
        arr.add(arr[it-1] + arr[it-2])
    }

    repeat(nextInt()) {
        println(arr[nextInt()+2])
    }
}.let { print(it) } }