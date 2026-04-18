import java.util.Scanner

fun main(): Unit = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val arr = (1..nextInt()).map { (1..it).map { nextInt() }.toMutableList() }

    if (arr.count() == 1) {
        appendLine(arr[0][0])

        return@buildString
    }

    // greedy from n-1 to 1
    (arr.count()-2 downTo 0).forEach { row ->
        repeat(arr[row].count()) { idx ->
            val children = listOf(arr[row+1][idx], arr[row+1][idx+1])

            arr[row][idx] += children.max()
        }
    }

    appendLine(arr[0][0])
}.let { print(it) } }