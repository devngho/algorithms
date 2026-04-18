import java.util.Scanner
import kotlin.math.abs

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val heap = MutableList(100_000) { Long.MIN_VALUE }
    val m = mutableMapOf<Long, Int>()
    var size = 0

    fun swap(a: Int, b: Int) {
        val temp = heap[b]
        heap[b] = heap[a]
        heap[a] = temp
    }

    repeat(nextInt()) {
        val v = nextLong()

        if (v == 0L) {
            if (size == 0) appendLine(0)
            else {
                appendLine(heap[0].let {
                    if (m.containsKey(it)) {
                        m[it] = m[it]!! - 1
                        if (m[it] == 0) m.remove(it)

                        -it
                    } else it
                })
                size--
                heap[0] = heap[size]
                heap[size] = Long.MIN_VALUE
                // trickle down
                var n = 0
                while (true) {
                    val left = 2 * n + 1
                    val right = 2 * n + 2
                    if (right >= 100_000) break

                    val smallerIdx = if (heap[left] == Long.MIN_VALUE && heap[right] == Long.MIN_VALUE) break else if(heap[right] == Long.MIN_VALUE) left else if (heap[left] > heap[right]) right else left
                    if (heap[n] < heap[smallerIdx]) break

                    swap(n, smallerIdx)
                    n = smallerIdx
                }
            }
        } else {
            heap[size] = abs(v)
            if (v < 0) m[abs(v)] = m.getOrDefault(abs(v), 0) + 1

            var n = size
            size++

            // bubble up
            while (n != 0 && heap[(n - 1) / 2] > abs(v)) { // while parent > v
                swap((n-1)/2, n)

                n = (n - 1) / 2
            }
        }

//        appendLine(heap.take(size))
    }
}.let { print(it) } }