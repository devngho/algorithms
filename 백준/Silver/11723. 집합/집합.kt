import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val n = nextLine().toInt()
    val map = mutableMapOf<String, Boolean>()

    (1..20).forEach { map[it.toString()] = false }

    (0 until n).forEach { _ ->
        val l = nextLine().split(" ")
        val op = l.first()

        when(op) {
            "add" -> map[l.last()] = true
            "remove" -> map[l.last()] = false
            "check" -> appendLine(if (map[l.last()]!!) 1 else 0)
            "toggle" -> map[l.last()] = !map[l.last()]!!
            "all" -> map.keys.forEach { map[it] = true }
            "empty" -> map.keys.forEach { map[it] = false }
            else -> throw UnsupportedOperationException("Unsupported operation $op")
        }
    }
}.let { print(it) } }