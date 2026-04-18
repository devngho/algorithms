import kotlin.math.pow
import kotlin.math.sqrt

fun main() = System.`in`.bufferedReader().let { reader -> buildString {
    // it can be proven that 3 arbitrary points can be selected
    val n = reader.readLine().toInt()
    val points = (1..n).map { reader.readLine().split(" ").map { it.toInt() } }

    fun distance(a: Int, b: Int) = sqrt((points[a][0] - points[b][0]).toDouble().pow(2) + (points[a][1] - points[b][1]).toDouble().pow(2))

    (0..<n).maxOfOrNull { a ->
        (a+1..<n).maxOfOrNull { b ->
            val ab = distance(a, b)
            (b+1..<n).maxOfOrNull { c ->
                val bc = distance(b, c)
                val ca = distance(a, c)

                val s = (ab+bc+ca)/2

                sqrt(s*(s-ab)*(s-bc)*(s-ca))
            } ?: 0.0
        } ?: 0.0
    }.let { appendLine(it) }
}.let { print(it) } }