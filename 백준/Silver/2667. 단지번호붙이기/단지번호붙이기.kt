package io.github.devngho.algorthmkt

import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    nextLine()
    val arr = List(n) { nextLine().toList() }
    val complex = List(n) { MutableList(n) { -1 } }

    fun dfs(x: Int, y: Int, complexId: Int): Int {
        if (arr[y][x] == '0') return 0

        return listOf(
            x to y,
            x+1 to y,
            x-1 to y,
            x to y+1,
            x to y-1
        ).filter {
            it.first in (0..<n) && it.second in (0..<n) && complex[it.second][it.first] == -1 && arr[it.second][it.first] == '1'
        }.also {
            it.forEach { v ->
                complex[v.second][v.first] = complexId
                dfs(v.first, v.second, complexId)
            }
        }.count()
    }

    var id = 1
    val counts = mutableListOf<Int>()

    repeat(n) { y ->
        repeat(n) { x->
            if (dfs(x, y, id) > 0) {
                id++
                counts.add(0)
            }

            if (complex[y][x] != -1) counts[complex[y][x]-1]++
        }
    }

    appendLine(counts.count())
    appendLine(counts.sorted().joinToString("\n"))
}.let { print(it) } }