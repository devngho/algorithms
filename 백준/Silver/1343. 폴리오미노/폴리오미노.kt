import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val board = nextLine().toMutableList()
    var i = 0
    val n = board.count()

    while (i < n) {
        if (board[i] == '.') {
            i++
            continue
        }

        if (i+4 <= n &&  (i..<i+4).all { board[it] == 'X' }) {
            (i..<i+4).forEach { board[it] = 'A' }
            i += 4
        } else if (i+2 <= n &&  (i..<i+2).all { board[it] == 'X' }) {
            (i..<i+2).forEach { board[it] = 'B' }
            i += 2
        } else {
            break
        }
    }

    if (i != n) appendLine(-1)
    else appendLine(board.joinToString(""))
}.let { print(it) } }