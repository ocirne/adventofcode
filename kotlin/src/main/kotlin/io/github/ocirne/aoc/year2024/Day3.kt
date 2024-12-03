package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day3(val lines: List<String>) : AocChallenge(2024, 3) {

    private val line = lines.joinToString(" ")

    override fun part1(): Int {
        return Regex("mul\\((\\d+),(\\d+)\\)")
            .findAll(line)
            .map { it.groupValues }
            .map { (_, x, y) -> x.toInt() * y.toInt() }
            .sum()
    }

    override fun part2(): Int {
        var result = 0
        var flag = true
        for (m in Regex("do\\(\\)|don't\\(\\)|mul\\((\\d+),(\\d+)\\)").findAll(line)) {
            when (m.groups[0]!!.value.substring(0, 3)) {
                "do(" -> flag = true
                "don" -> flag = false
                "mul" -> if (flag) result += m.groupValues[1].toInt() * m.groupValues[2].toInt()
            }
        }
        return result
    }
}
