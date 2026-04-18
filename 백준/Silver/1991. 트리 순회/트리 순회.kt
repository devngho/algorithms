import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val nodes = mutableListOf<String>()
    val left = mutableMapOf<String, String>()
    val right = mutableMapOf<String, String>()
    repeat(nextInt().also { nextLine() }) {
        val (n, l, r) = nextLine().split(" ")

        nodes.add(n)
        left[n] = if (l == ".") "" else l
        right[n] = if (r == ".") "" else r
    }

    fun leftTraverse(node: String): String = if (node != "") node+leftTraverse(left[node]!!)+leftTraverse(right[node]!!) else ""
    fun middleTraverse(node: String): String = if (node != "") middleTraverse(left[node]!!)+node+middleTraverse(right[node]!!) else ""
    fun rightTraverse(node: String): String = if (node != "") rightTraverse(left[node]!!)+rightTraverse(right[node]!!)+node else ""

    appendLine(leftTraverse("A"))
    appendLine(middleTraverse("A"))
    appendLine(rightTraverse("A"))

}.let { print(it) } }