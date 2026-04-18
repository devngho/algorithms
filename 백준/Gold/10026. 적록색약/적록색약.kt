import java.util.LinkedList
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) {
    val delta = listOf(0 to 1, 0 to -1, 1 to 0, -1 to 0)

    fun countChunk(n: Int, grid: List<MutableList<Char>>): Int {
        var chunks = 0

        (0 until n).forEach { y ->
            (0 until n).forEach { x ->
                val color = grid[y][x]
                if (color == 'V') return@forEach // visited

                val q = LinkedList(listOf(x to y))
                while(q.isNotEmpty()) {
                    val v = q.pop()
                    delta.forEach { d ->
                        val p = v.first + d.first to v.second + d.second

                        if (p.first !in 0..<n || p.second !in 0..<n) return@forEach
                        if (grid[p.second][p.first] != color) return@forEach

                        grid[p.second][p.first] = 'V'
                        q.add(p)
                    }
                }

                chunks++
            }
        }

        return chunks
    }

    fun solve(n: Int, arr: List<List<Char>>): Pair<Int, Int> {
        val gridNonWeak = arr.map { it.toMutableList() }.toMutableList()
        val gridWeak = arr.map { it.map { if (it == 'G') 'R' else it }.toMutableList() }.toMutableList()

        return countChunk(n, gridNonWeak) to countChunk(n, gridWeak)
    }

    val n = nextInt()

    nextLine()

    println(solve(n, (1..n).map { nextLine().toList() }).toList().joinToString(" "))
}