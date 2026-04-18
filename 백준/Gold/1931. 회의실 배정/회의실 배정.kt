import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val meetings = mutableListOf<Pair<Int, Int>>()

    (0 until n).forEach { _ -> meetings.add(nextInt() to nextInt()) }

    meetings.sortBy { it.first }
    meetings.sortBy { it.second }

    var m = 0
    var res = 0

    (0 until n).forEach { i ->
        if (meetings[i].first /* a */ < m) return@forEach

        res++
        m = meetings[i].second /* b */
    }

    println(res)
}