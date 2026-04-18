fun main(): Unit = with(System.`in`.bufferedReader()) { buildString {
    val n = this@with.readLine().toInt()

    if (n == 1) {
        val arr = this@with.readLine().split(" ").map { it.toInt() }
        appendLine("${arr.max()} ${arr.min()}")

        return@buildString
    }

    val d = listOf(listOf(0, 1), listOf(0, 1, 2), listOf(1, 2))
    val tmp1 = mutableListOf(0, 0, 0)
    val tmp2 = mutableListOf(0, 0, 0)
    val arr1 = mutableListOf(0, 0, 0)
    val arr2 = mutableListOf(0, 0, 0)

    repeat(n) {
        val arr = this@with.readLine().split(" ").map { it.toInt() }

        repeat(3) { idx ->
            tmp1[idx] = arr[idx] + d[idx].maxOf { arr1[it] }
            tmp2[idx] = arr[idx] + d[idx].minOf { arr2[it] }
        }

        repeat(3) { idx ->
            arr1[idx]=tmp1[idx]
            arr2[idx]=tmp2[idx]
        }
    }

    appendLine("${arr1.max()} ${arr2.min()}")
}.let { print(it) } }