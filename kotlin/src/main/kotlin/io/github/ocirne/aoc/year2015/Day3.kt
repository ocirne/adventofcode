package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day3(val lines: List<String>) : AocChallenge(2015, 3) {

    private fun move(c: Char, pos: Pair<Int, Int>): Pair<Int, Int> {
        return when (c) {
            '>' -> Pair(pos.first + 1, pos.second)
            '<' -> Pair(pos.first - 1, pos.second)
            '^' -> Pair(pos.first, pos.second - 1)
            'v' -> Pair(pos.first, pos.second + 1)
            else -> throw Exception()
        }
    }

    fun solve1(line: String): Int {
        var pos = Pair(0, 0)
        val houses = mutableSetOf(pos)
        line.forEach { c ->
            pos = move(c, pos)
            houses.add(pos)
        }
        return houses.size
    }

    override fun part1(): Int {
        return solve1(lines.first())
    }

    fun solve2(line: String): Int {
        var sPos = Pair(0, 0)
        var rPos = Pair(0, 0)
        val houses = mutableSetOf(0 to 0)
        line.forEachIndexed { index, c ->
            if (index % 2 == 0) {
                sPos = move(c, sPos)
                houses.add(sPos)
            } else {
                rPos = move(c, rPos)
                houses.add(rPos)
            }
        }
        return houses.size
    }

    override fun part2(): Int {
        return solve2(lines.first())
    }
}
