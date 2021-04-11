package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day9(val lines: List<String>) : AocChallenge(2015, 8) {

    private val literals = lines.map(String::trim)

    override fun part1(): Int {
        return literals.map(this::shrink).sum()
    }

    override fun part2(): Int {
        return literals.map(this::expand).sum()
    }

    fun shrink(line: String): Int {
        var result = 0
        var i = 0
        while (i < line.length) {
            val c = line[i]
            if (c != '"' || !(i == 0 || i + 1 == line.length)) {
                if (c == '\\') {
                    i += when {
                        line[i + 1] == '\\' || line[i + 1] == '"' -> 1
                        line[i + 1] == 'x' && line[i + 2].isLetterOrDigit() && line[i + 3].isLetterOrDigit() -> 3
                        else -> throw Exception()
                    }
                }
                result++
            }
            i++
        }
        return line.length - result
    }

    fun expand(line: String): Int {
        return 2 + line.map { c -> if (c == '"' || c == '\\') 1 else 0 }.sum()
    }
}
