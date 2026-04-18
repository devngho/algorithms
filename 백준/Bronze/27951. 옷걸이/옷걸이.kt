// random marathon 6
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val a = List(n) { it to nextInt() }
    val aSorted = a.sortedBy { it.second }

    var up = nextInt()
    var down = nextInt()

    val res: List<Pair<Int, Char>>? = (res@{ aSorted.map { (k, v) ->
        when (v) {
            1 -> {
                if (up >= 1) {
                    up -= 1
                    k to 'U'
                } else return@res null
            }
            2 -> {
                if (down >= 1) {
                    down -= 1
                    k to 'D'
                } else return@res null
            }
            3 -> {
                if (up >= 1) {
                    up -= 1
                    k to 'U'
                } else if (down >= 1) {
                    down -= 1
                    k to 'D'
                } else return@res null
            }
            else -> return@res null
        }
    } })()

    if (res == null) {
        appendLine("NO")
    } else {
        appendLine("YES")
        val resIndexed = res.sortedBy { it.first }
        resIndexed.forEach { append(it.second) }
        appendLine()
    }
}.let { print(it) } }