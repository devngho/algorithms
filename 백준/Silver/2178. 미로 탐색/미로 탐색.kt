package io.github.devngho.algorthmkt

import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val m = nextInt()
    nextLine()

    val arr = List(n) {
        nextLine().toList()
    }

    val visited: MutableList<MutableList<Boolean>> = MutableList(n) { MutableList(m) { false } }
    val q = ArrayDeque<Triple<Int, Int, Int>>(listOf(Triple(0, 0, 0)))

    fun isOK(x: Int, y: Int): Boolean {
        if (x < 0 || y < 0 || x >= m || y >= n) return false

        if (arr[y][x] == '0') return false
        if (visited[y][x]) return false

        return true
    }

    var distance: Int

    while (true) {
        val (x, y, d) = q.removeFirst()

        if (x == m-1 && y == n-1) {
            distance = d+1
            break
        }

        val next = listOf(
            x+1 to y,
            x to y+1,
            x-1 to y,
            x to y-1
        )

        next.filter { isOK(x, y) }.forEach {
            visited[y][x]=true
            q.add(Triple(it.first, it.second, d+1))
        }
    }

    appendLine(distance)
}.let { print(it) } }