// random marathon 4
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    nextLine().let { s ->
        if (s.contains('A')) s.replace('B', 'A').replace('C', 'A').replace('D', 'A').replace('F', 'A')
        else if (s.contains('B')) s.replace('C', 'B').replace('D', 'B').replace('F', 'B')
        else if (s.contains('C')) s.replace('D', 'C').replace('F', 'C')
        else (1..s.count()).fold("") { r, _ -> r + 'A' }
    }.let { appendLine(it) }
}.let { print(it) } }