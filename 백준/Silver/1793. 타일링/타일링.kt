import java.util.Scanner
import java.math.BigInteger

fun main() = with(Scanner(System.`in`.bufferedReader())) {
    val arr = mutableListOf<Int>()
    while (hasNextInt()) {
        arr.add(nextInt())
    }
    val n = arr.max()
    val two = BigInteger.valueOf(2)

    val dp = MutableList(n+1) { BigInteger.ONE }

    (2..n).forEach {
        dp[it] = (dp[it - 1] + dp[it-2]*two)
    }
    
    arr.forEach {
        println(dp[it])
    }
}