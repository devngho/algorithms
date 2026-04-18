// random marathon 1
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val m = nextInt()
    val k = nextInt()

    print(if(m % k == 0) "Yes" else "No")
}.let { print(it) } }