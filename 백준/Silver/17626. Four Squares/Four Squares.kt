import java.util.Scanner
import kotlin.math.floor
import kotlin.math.pow
import kotlin.math.sqrt

fun main() = with(Scanner(System.`in`.bufferedReader())) {
    fun solve(n: Int): Int {
        val dp = IntArray(n+1) { Int.MAX_VALUE }
         (1..floor(sqrt(n.toDouble())).toInt()).forEach { dp[it.toDouble().pow(2).toInt()] = 1 }

        (1..n).forEach { num ->
            if (dp[num] != Int.MAX_VALUE) return@forEach

            val d = floor(sqrt(num.toDouble())).toInt()

            dp[num] = (1..d).minOf {
                dp[num-it.toDouble().pow(2).toInt()]
            } + 1
        }

        return dp[n]
    }

    println(solve(nextInt()))
}