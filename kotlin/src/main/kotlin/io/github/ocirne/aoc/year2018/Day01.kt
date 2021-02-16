package io.github.ocirne.aoc.year2018

class Day01(private val lines: List<String>) {

    fun part1(): Int {
        return lines.map { it.toInt() }.sum()
    }
}