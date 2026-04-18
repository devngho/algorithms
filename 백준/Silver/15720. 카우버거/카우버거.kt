// random marathon 7
import java.util.Scanner

fun main() = with(Scanner(System.`in`.bufferedReader())) { buildString {
    val b = nextInt()
    val c = nextInt()
    val d = nextInt()

    val burgers = List(b) { nextInt() }.sorted().reversed().toMutableList()
    val sides = List(c) { nextInt() }.sorted().reversed().toMutableList()
    val drinks = List(d) { nextInt() }.sorted().reversed().toMutableList()

    appendLine(burgers.sum() + sides.sum() + drinks.sum())

    val maxSets = listOf(burgers.count(), sides.count(), drinks.count()).min()

    (0 until maxSets).forEach {
        burgers[it] = (burgers[it] * 0.9).toInt()
        sides[it] = (sides[it] * 0.9).toInt()
        drinks[it] = (drinks[it] * 0.9).toInt()
    }

    appendLine(burgers.sum() + sides.sum() + drinks.sum())
}.let { print(it) } }