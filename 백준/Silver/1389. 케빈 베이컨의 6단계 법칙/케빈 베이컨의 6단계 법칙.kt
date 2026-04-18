package io.github.devngho.algorthmkt

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
                *((1..n).map { k -> k to 100000 }.toTypedArray())
            )
        }.toTypedArray())
    )

    graph.forEach {
        d[it[0]]!![it[1]] = 1
        d[it[1]]!![it[0]] = 1
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
    
    val bacon = mutableMapOf(
        *((1..n).map { k -> k to 0 }.toTypedArray())
    )

    (1..n).forEach { start ->
        (1..n).forEach { end ->
            if (start == end) return@forEach

            bacon[start] = bacon[start]!! + d[start]!![end]!!
        }
    }

    appendLine(bacon.minBy { it.value }.key)
}.let { print(it) } }