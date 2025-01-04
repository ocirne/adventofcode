package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.combinationsOfTwo

class Day8(val lines: List<String>) : AocChallenge(2024, 8) {

    override fun part1(): Int {
        val width = lines.first().length
        val height = lines.size
        val antennas = mutableMapOf<Char, MutableList<Pair<Int, Int>>>()
        lines.mapIndexed { y, line ->
            line.mapIndexed { x, value ->
                if (value != '.') {
                    if (!antennas.contains(value)) {
                        antennas[value] = mutableListOf()
                    }
                    antennas[value]!!.add(x to y)
                }
            }
        }
        val antinodes = mutableSetOf<Pair<Int, Int>>()
        antennas.map { (_, positions) ->
            positions.combinationsOfTwo().forEach { (p1, p2) ->
                val (x1, y1) = p1
                val (x2, y2) = p2
                val dx = x2 - x1
                val dy = y2 - y1
                antinodes.add(x1 - dx to y1 - dy)
                antinodes.add(x2 + dx to y2 + dy)
            }
        }
        return antinodes.filter { (x, y) -> x in 0 until width && y in 0 until height }.size
    }

    override fun part2(): Int {
        val width = lines.first().length
        val height = lines.size
        val antennas = mutableMapOf<Char, MutableList<Pair<Int, Int>>>()
        lines.mapIndexed { y, line ->
            line.mapIndexed { x, value ->
                if (value != '.') {
                    if (!antennas.contains(value)) {
                        antennas[value] = mutableListOf()
                    }
                    antennas[value]!!.add(x to y)
                }
            }
        }
        val antinodes = mutableSetOf<Pair<Int, Int>>()
        antennas.map { (_, positions) ->
            positions.combinationsOfTwo().forEach { (p1, p2) ->
                val (x1, y1) = p1
                val (x2, y2) = p2
                val dx = x2 - x1
                val dy = y2 - y1
                for (f in 0 .. 100) {
                    antinodes.add(x1 - f * dx to y1 - f * dy)
                    antinodes.add(x2 + f * dx to y2 + f * dy)
                }
            }
        }
        return antinodes.filter { (x, y) -> x in 0 until width && y in 0 until height }.size
    }
}
