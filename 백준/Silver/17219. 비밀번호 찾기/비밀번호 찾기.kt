import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val m = nextInt()
    nextLine()

    val pw = mutableMapOf<String, String>()

    repeat(n) {
        val line = nextLine().split(" ")
        pw[line[0]] = line[1]
    }

    repeat(m) {
        println(pw[nextLine()])
    }
}.let { print(it) } }