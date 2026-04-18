import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val m = nextInt()
    nextLine()
    val graph = (1..m).map {
        nextLine().split(" ").map { it.toInt() }
    }

    // floyd-warshall
    val d = mapOf(
        *((1..n).map {
            it to mutableMapOf(
                *((1..n).map { k -> k to if (it != k) 100_000_000 else 0 }.toTypedArray())
            )
        }.toTypedArray())
    )

    graph.forEach {
        if (d[it[0]]!![it[1]]!! > it[2]) d[it[0]]!![it[1]] = it[2]
    }

    (1..n).forEach { mid ->
        (1..n).forEach { start ->
            (1..n).forEach { end ->
                if (d[start]!![end]!! > d[start]!![mid]!! + d[mid]!![end]!!) {
                    d[start]!![end] = d[start]!![mid]!! + d[mid]!![end]!!
                }
            }
        }
    }

    appendLine(d.values.joinToString("\n") {
        it.values.joinToString(" ") { v -> if (v != 100_000_000) "$v" else "0" }
    })
}.let { print(it) } }