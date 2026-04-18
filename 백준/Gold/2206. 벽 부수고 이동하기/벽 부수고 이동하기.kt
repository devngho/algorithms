fun main() = System.`in`.bufferedReader().let { reader -> buildString {
    data class Path(val x: Int, val y: Int, val d: Int, val broken: Boolean)

    val (n, m) = reader.readLine().split(" ").map { it.toInt() }

    val arr = List(n) {
        reader.readLine().toList()
    }

    val visited = MutableList(n) { MutableList(m) { false to false } } // not yet broken, broken
    val q = ArrayDeque(listOf(Path(0, 0, 0, false)))

    fun isOK(x: Int, y: Int, broken: Boolean): Boolean {
        if (x < 0 || y < 0 || x >= m || y >= n) return false

        if (arr[y][x] == '1' && broken) return false
        if (broken && visited[y][x].second || !broken && visited[y][x].first) return false

        return true
    }

    var distance: Int = -1

    while (q.isNotEmpty()) {
        val (px, py, d, b) = q.removeFirst()

        if (px == m-1 && py == n-1) {
            distance = d+1
            break
        }

        val next = listOf(
            px+1 to py,
            px to py+1,
            px-1 to py,
            px to py-1
        )

        next.filter { isOK(it.first, it.second, b) }.forEach { (x, y) ->
            if (arr[y][x] == '1') {
                q.add(Path(x, y, d+1, true))
                visited[y][x] = visited[y][x].first to true
            } else {
                q.add(Path(x, y, d+1, b))
                if (b) visited[y][x] = visited[y][x].first to true
                else   visited[y][x] = true to visited[y][x].second
            }
        }
    }

    appendLine(distance)
}.let { print(it) } }