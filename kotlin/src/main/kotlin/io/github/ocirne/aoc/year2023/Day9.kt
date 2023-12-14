package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge

class Day9(val lines: List<String>) : AocChallenge(2023, 9) {

    fun nextValue(a: List<Int>, r: Int): Int = a.last() + r

    fun previousValue(a: List<Int>, r: Int): Int = a.first() - r

    private fun rec(a: List<Int>, f: (a: List<Int>, rest: Int) -> Int): Int {
        if (a.all { it == 0 }) {
            return 0
        }
        val differences = a.zipWithNext { p, s -> s - p }
        val d = rec(differences, f)
        return f(a, d)
    }

    fun adjacentValue(line: String, f: (a: List<Int>, rest: Int) -> Int): Int {
        return rec(line.split(' ').map { it.toInt() }, f)
    }

    private fun sumAdjacentValues(f: (a: List<Int>, rest: Int) -> Int): Int {
        return lines.sumOf { line -> adjacentValue(line, f) }
    }

    override fun part1(): Int {
        return sumAdjacentValues(this::nextValue)
    }

    override fun part2(): Int {
        return sumAdjacentValues(this::previousValue)
    }
}
