package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day19(val lines: List<String>) : AocChallenge(2024, 19) {

    private class DesignCounter(private val towels: List<String>) {

        private val cache = mutableMapOf<String, Long>()

        fun countPossible(design: String): Long {
            if (design in cache) {
                return cache[design]!!
            }
            if (design.isEmpty()) {
                return 1L
            }
            val result = towels
                .filter { towel -> design.startsWith(towel) }
                .sumOf { towel -> countPossible(design.drop(towel.length)) }
            cache[design] = result
            return result
        }
    }

    private fun analyzeAllDesigns(): List<Long> {
        val towels = lines.first().split(", ")
        return lines.drop(2).map { design -> DesignCounter(towels).countPossible(design) }
    }

    override fun part1(): Int {
        return analyzeAllDesigns().count { it > 0 }
    }

    override fun part2(): Long {
        return analyzeAllDesigns().sum()
    }
}
