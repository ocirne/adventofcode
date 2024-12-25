package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.combinationsOfTwo

class Day25(val lines: List<String>) : AocChallenge(2024, 25) {

    private data class Position(val x: Int, val y: Int)

    private fun readGrid(gridLines: List<String>): Set<Position> {
        val s = mutableSetOf<Position>()
        gridLines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                if (c == '#') {
                    s.add(Position(x, y))
                }
            }
        }
        return s.toSet()
    }

    override fun part1(): Int {
        return lines
            .chunked(8)
            .map(::readGrid)
            .combinationsOfTwo()
            .count { (p1, p2) -> p1.intersect(p2).isEmpty() }
    }

    override fun part2(): Int {
        return -1
    }
}
