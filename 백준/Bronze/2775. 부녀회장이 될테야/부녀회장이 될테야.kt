import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    repeat(nextInt()) {
        val (k, n) = nextInt() to nextInt()

        val apartment = List(k + 1) { floor -> MutableList(n) { if (floor == 0) it + 1 else 0 } } // a층 b호 -> apartment[a][b-1]

        (1..k).forEach { floor ->
            var s = 0

            (0..n-1).forEach { room ->
                s += apartment[floor-1][room]

                apartment[floor][room] = s
            }
        }
        
        appendLine(apartment[k][n-1])
    }
}.let { print(it) } }