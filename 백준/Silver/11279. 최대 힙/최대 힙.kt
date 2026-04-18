package io.github.devngho.algorthmkt

import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val heap = MutableList(100_000) { -1 }
    var size = 0

    fun swap(a: Int, b: Int) {
        val temp = heap[b]
        heap[b] = heap[a]
        heap[a] = temp
    }

    repeat(nextInt()) {
        val v = nextInt()

        if (v == 0) {
            if (size == 0) appendLine(0)
            else {
                appendLine(heap[0])
                size--
                heap[0] = heap[size]
                heap[size] = -1
                // trickle down
                var n = 0
                while (true) {
                    val left = 2 * n + 1
                    val right = 2 * n + 2
                    if (right >= 100_000) break

                    val smallerIdx = if (heap[left] == -1 && heap[right] == -1) break else if(heap[right] == -1) left else if (heap[left] < heap[right]) right else left
                    if (heap[n] > heap[smallerIdx]) break

                    swap(n, smallerIdx)
                    n = smallerIdx
                }
            }
        } else {
            heap[size] = v
            var n = size
            size++

            // bubble up
            while (n != 0 && heap[(n - 1) / 2] < v) { // while parent < v
                swap((n-1)/2, n)

                n = (n - 1) / 2
            }
        }

//        println(heap.take(size))
    }
}.let { print(it) } }