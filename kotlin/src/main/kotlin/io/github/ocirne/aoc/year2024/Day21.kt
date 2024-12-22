package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day21(val lines: List<String>) : AocChallenge(2024, 21) {

    val positionsNumericKeypad = mapOf(
        '1' to Pair(0, 2),
        '2' to Pair(1, 2),
        '3' to Pair(2, 2),
        '4' to Pair(0, 1),
        '5' to Pair(1, 1),
        '6' to Pair(2, 1),
        '7' to Pair(0, 0),
        '8' to Pair(1, 0),
        '9' to Pair(2, 0),
        '0' to Pair(1, 3),
        'A' to Pair(2, 3),
    )

    val positionsDirectionalKeypad = mapOf(
        '^' to Pair(1, 0),
        'A' to Pair(2, 0),
        '<' to Pair(0, 1),
        'v' to Pair(1, 1),
        '>' to Pair(2, 1),
    )

    fun countMoves(): Int {
        return -1
    }


    override fun part1(): Int {
        return -1
    }

    override fun part2(): Int {
        return -1
    }
}
