package io.github.devngho.algorthmkt

import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextInt()
    val m = nextInt()
    val snakes = List(n) { nextInt() to nextInt() }.toMap()
    val ladders = List(m) { nextInt() to nextInt() }.toMap()
    val queue = ArrayDeque(listOf(1 to 0))
    val visited = MutableList(110) { false }

    // bfs
    while (queue.isNotEmpty()) {
        val (pos, t) = queue.removeFirst()

        if (pos == 100) {
            appendLine(t)
            break
        }

        listOf(pos+1, pos+2, pos+3, pos+4, pos+5, pos+6).filterNot {
            visited[it-1]
        }.map {
            when (it) {
                in snakes -> snakes[it]
                in ladders -> ladders[it]
                else -> it
            } as Int
        }.forEach {
            visited[it-1] = true
            queue.add(it to t+1)
        }
    }
}.let { print(it) } }