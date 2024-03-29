package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day2(lines: List<String>) : AocChallenge(2015, 2) {

    private val presents = lines.map { line -> line.split("x").map(String::toInt).sorted() }

    override fun part1(): Int {
        return presents.sumOf { (h, l, w) -> 3 * h * l + 2 * h * w + 2 * l * w }
    }

    override fun part2(): Int {
        return presents.sumOf { (h, l, w) -> 2 * (h + l) + h * l * w }
    }
}
