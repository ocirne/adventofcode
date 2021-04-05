package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.max

class Day6(val lines: List<String>) : AocChallenge(2015, 6) {

    override fun part1(): Int {
        return run({ (it + 1) % 2 }, { 1 }) { 0 }
    }

    override fun part2(): Int {
        return run({ it + 2 }, { it + 1 }) { max(0, it - 1) }
    }

    private fun turn(grid: MutableMap<Pair<Int, Int>, Int>, action: (Int) -> Int, startXY: String, endXY: String) {
        val sxy = startXY.toPair()
        val exy = endXY.toPair()
        for (x in sxy.first..exy.first) {
            for (y in sxy.second..exy.second) {
                val p = Pair(x, y)
                val value = grid.getOrDefault(p, 0)
                grid[p] = action.invoke(value)
            }
        }
    }

    private fun run(toggle: (Int) -> Int, turn_on: (Int) -> Int, turn_off: (Int) -> Int): Int {
        val grid = mutableMapOf<Pair<Int, Int>, Int>()
        lines.forEach { line ->
            val token = line.split(' ')
            when {
                line.startsWith("toggle") -> turn(grid, toggle, token[1], token[3])
                line.startsWith("turn on") -> turn(grid, turn_on, token[2], token[4])
                line.startsWith("turn off") -> turn(grid, turn_off, token[2], token[4])
            }
        }
        return grid.values.sum()
    }

    private fun String.toPair(): Pair<Int, Int> {
        val pair = this.split(',').map { s -> s.toInt() }
        return Pair(pair[0], pair[1])
    }
}
