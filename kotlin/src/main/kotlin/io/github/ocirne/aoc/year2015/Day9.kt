package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

fun <T> List<T>.permutations(): List<List<T>> {
    if (this.size <= 1) {
        return listOf(this)
    }
    val result = ArrayList<List<T>>()
    this.forEachIndexed { index, pivot ->
        val rest = this.without(index)
        rest.permutations().forEach { permutation ->
            result.add(listOf(pivot) + permutation)
        }
    }
    return result
}

fun <T> List<T>.without(index: Int): List<T> {
    val copy = this.toMutableList()
    copy.removeAt(index)
    return copy.toList()
}

typealias Edge = Pair<String, String>

typealias Route = List<String>

class Day9(val lines: List<String>) : AocChallenge(2015, 9) {

    private val locations = HashSet<String>()

    private val distances = HashMap<Edge, Int>()

    init {
        lines.forEach { line ->
            val (start, _, dest, _, distance) = line.split(' ')
            locations.add(start)
            locations.add(dest)
            distances[start to dest] = distance.toInt()
            distances[dest to start] = distance.toInt()
        }
    }

    override fun part1(): Int {
        return run().minOrNull()!!
    }

    override fun part2(): Int {
        return run().maxOrNull()!!
    }

    private fun calcDistance(route: Route): Int {
        return route.zipWithNext { from, to -> distances[from to to]!! }.sum()
    }

    private fun run(): List<Int> {
        return locations.toList().permutations().map { route -> calcDistance(route) }
    }
}
