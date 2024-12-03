package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day3(val lines: List<String>) : AocChallenge(2024, 3) {

    override fun part1(): Int {
        val line = lines.joinToString(" ")

        val regex = Regex("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)")
        val matches = regex.findAll(line)
        val names = matches.map { it.groupValues }.map { (_, x, y) -> x.toInt() * y.toInt() }.sum()
        return names
    }

    override fun part2(): Int {
        val line = lines.joinToString(" ")

        val regex = Regex("do\\(\\)|don't\\(\\)|mul\\(([0-9]{1,3}),([0-9]{1,3})\\)")
        val matches = regex.findAll(line)
        var result = 0
        var flag = true
        for (m in matches) {
            when (m.groups[0]!!.value.substring(0, 3)) {
                "do(" -> flag = true
                "don" -> flag = false
                "mul" -> if (flag) result += m.groupValues[1].toInt() * m.groupValues[2].toInt()
            }
        }
        return result
    }
}
