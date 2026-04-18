import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val f = nextInt()

    val num = n - (n % 100)
    var res = "00"

    r@ for (a in (0..9)) {
        for (b in (0..9)) {
            if ((num + 10*a + b) % f == 0) {
                res = "$a$b"
                break@r
            }
        }
    }

    appendLine(res)
}.let { print(it) } }