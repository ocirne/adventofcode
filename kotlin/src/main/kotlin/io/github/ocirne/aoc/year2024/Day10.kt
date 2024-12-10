package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day10(val lines: List<String>) : AocChallenge(2024, 10) {

    fun search(trails: Map<Pair<Int, Int>, Int>, width: Int, height: Int, position: Pair<Int, Int>): Long {
        val value = trails[position]!!
        if (value == 9) {
            if (!foo.contains(position)) {
                foo.put(position, 0)
            }
            foo[position] = foo[position]!! + 1
            return 1
        }
        var total = 0L
        val (x, y) = position
        for ((nx, ny) in listOf(x-1 to y, x+1 to y, x to y-1, x to y+1)) {
            if (nx < 0 || width <= nx || ny < 0 || height <= ny)
                continue
            if (trails[nx to ny] != value + 1) {
                continue
            }
            total += search(trails, width, height, nx to ny)
        }
        return total
    }

    var foo = mutableMapOf<Pair<Int, Int>, Int>()

    override fun part1(): Long {
        val width = lines.first().length
        val height = lines.size
        val trails = mutableMapOf<Pair<Int, Int>, Int>()
        lines.mapIndexed { y, line ->
            line.mapIndexed { x, value ->
                trails[x to y] = value.digitToInt()
            }
        }
        var total = 0L
        trails.map { start ->
            if (start.value == 0) {
                foo.clear()
                search(trails, width, height, start.key)
                total += foo.size
                println(foo.size)
            }
        }
        return total
    }

    override fun part2(): Long {
        val width = lines.first().length
        val height = lines.size
        val trails = mutableMapOf<Pair<Int, Int>, Int>()
        lines.mapIndexed { y, line ->
            line.mapIndexed { x, value ->
                trails[x to y] = value.digitToInt()
            }
        }
        var total = 0L
        trails.map { start ->
            if (start.value == 0) {
                foo.clear()
                search(trails, width, height, start.key)
                total += foo.map { it.value }.sum()
                println(foo.size)
            }
        }
        return total
    }
}
