import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val str = nextLine()
    val n = str.count()
    val cnt = str.toList().distinct().associateWith { str.count { c -> c == it } }.toMutableMap()
    val odds = cnt.count { it.value % 2 == 1 }

    if ((odds != 1 && n%2==1) || (odds != 0 && n%2==0)) {
        appendLine("I'm Sorry Hansoo")
        return@buildString
    }

    val list = MutableList(n) { ' ' }
    var odd = ' '
    var i = 0

    cnt.keys.sorted().forEach {
        while (cnt[it]!! >= 2) {
            list[i] = it
            list[n - i - 1] = it
            i += 1
            cnt[it] = cnt[it]!! - 2
        }

        if (cnt[it] == 1) odd = it
    }

    if (n % 2 == 1) list[i] = odd

    appendLine(list.joinToString(""))
}.let { print(it) } }