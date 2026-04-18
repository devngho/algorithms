fun main() = with(System.`in`.bufferedReader()) { buildString {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val titles = List(n) { readLine().split(" ").let { it[0] to it[1].toInt() } }.distinctBy { it.second }.let {
        it.mapIndexed { index, pair -> Triple(pair.first, if (index != 0) it[index-1].second else -1, pair.second) }
    }

    repeat(m) {
        val power = readLine().toInt()
        appendLine(titles[titles.binarySearch { if (power <= it.second) 1 else if (power > it.third) -1 else 0 }].first)
    }
}.let { print(it) } }