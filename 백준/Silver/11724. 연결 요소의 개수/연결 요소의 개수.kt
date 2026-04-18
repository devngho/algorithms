import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val m = nextInt()

    val graph = mutableMapOf<Int, MutableList<Int>>()

    (1..n).forEach { graph[it] = mutableListOf() }

    (0 until m).forEach {
        val u = nextInt()
        val v = nextInt()

        graph[u]!!.add(v)
        graph[v]!!.add(u)
    }

    var res = 0
    val visited = mutableSetOf<Int>()

    (1..n).forEach {
        if (visited.contains(it)) return@forEach

        res++

        val q = ArrayDeque<Int>()

        q.add(it)

        while (q.isNotEmpty()) {
            val u = q.removeFirst()

            visited.add(u)

            graph[u]!!.filterNot { v -> visited.contains(v) }.forEach { v ->
                visited.add(v)
                q.add(v)
            }
        }
    }

    appendLine(res)
}.let { print(it) } }