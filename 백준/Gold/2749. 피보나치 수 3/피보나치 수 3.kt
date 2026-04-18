import java.math.BigInteger
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    var n = nextBigInteger()
    val mod = BigInteger.valueOf(1_000_000)

    fun matrixMultiply(a: List<List<BigInteger>>, b: List<List<BigInteger>>): List<List<BigInteger>> = listOf(
        listOf((a[0][0]*b[0][0] % mod +a[1][0 ]*b[0][1] % mod), (a[0][1]*b[0][0]+a[1][1]*b[0][1]) % mod),
        listOf((a[0][0]*b[1][0]% mod+a[1][0]*b[1][1]) % mod, (a[0][1]*b[1][0]+a[1][1]*b[1][1]) % mod),
    )

    val matrix = listOf(listOf(BigInteger.ONE, BigInteger.ONE), listOf(BigInteger.ONE, BigInteger.ZERO))
    val arr = mutableListOf(matrix)

    val binaries = mutableListOf<Boolean>()
    val two = BigInteger.ONE + BigInteger.ONE

    while (n > BigInteger.ZERO) {
        binaries.add(n.mod(two) == BigInteger.ONE)
        n /= two
    }

    repeat(binaries.count()) {
        arr.add(matrixMultiply(arr.last(), arr.last()))
    }

    var result = matrix

    binaries.forEachIndexed { idx, v ->
        if (v) result = matrixMultiply(result, arr[idx])
    }

    appendLine(result[1][1])
}.let { print(it) } }