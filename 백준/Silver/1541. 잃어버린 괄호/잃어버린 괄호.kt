import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) {
    fun solve(exp: String): Int {
        var isMinus = false
        var tmp = 0
        var res = 0

        exp.forEach {
            if (it.isDigit()) {
                tmp *= 10
                tmp += it.digitToInt()
            } else {
                if (isMinus) res -= tmp
                else res += tmp

                tmp = 0

                if (it == '-') isMinus = true
            }
        }

        if (isMinus) res -= tmp
        else res += tmp

        return res
    }

    println(solve(nextLine()))
}