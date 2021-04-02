package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day3(lines: List<String>) : AocChallenge(2015, 3) {

    private val line = lines[0]

    private fun move(c: Char, pos: Pair<Int, Int>): Pair<Int, Int> {
        return when (c) {
            '>' -> Pair(pos.first + 1, pos.second)
            '<' -> Pair(pos.first - 1, pos.second)
            '^' -> Pair(pos.first, pos.second - 1)
            'v' -> Pair(pos.first, pos.second + 1)
            else -> throw Exception()
        }
    }

    override fun part1(): Int {
        var pos = Pair(0, 0)
        val houses = mutableSetOf(pos)
        line.forEach { c ->
            pos = move(c, pos)
            houses.add(pos)
        }
        return houses.size
    }

    override fun part2(): Int {
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
}
