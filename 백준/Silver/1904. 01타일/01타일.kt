import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) {
    fun solve(n: Int): Int {
        val dp = MutableList(n+1) { 1 }

        (2..n).forEach {
            dp[it] = (dp[it - 1] + dp[it-2]) % 15746
        }

        return dp[n]
    }

    println(solve(nextInt()))
}