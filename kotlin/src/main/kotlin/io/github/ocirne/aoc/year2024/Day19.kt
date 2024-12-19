package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day19(val lines: List<String>) : AocChallenge(2024, 19) {

    private fun isPossible(towels: List<String>, design: String): Boolean {
        if (design.isEmpty()) {
            return true
        }
        for (towel in towels) {
            if (design.startsWith(towel)) {
                val restDesign = design.drop(towel.length)
                if (isPossible(towels, restDesign)) {
                    return true;
                }
            }
        }
        return false
    }

    override fun part1(): Int {
        val towels = lines.first().split(", ")
        println(towels)
        println()
        var total = 0
        for (design in lines.drop(2)) {
            println(design)
            val t = isPossible(towels, design)
            println(t)
            if (t)
                total += 1
        }
        return total
    }

    private val cache = mutableMapOf<String, Long>()

    private fun countPossible(towels: List<String>, design: String): Long {
        if (design in cache) {
            return cache[design]!!
        }
        if (design.isEmpty()) {
            return 1L
        }
        var total = 0L
        for (towel in towels) {
            if (design.startsWith(towel)) {
                val restDesign = design.drop(towel.length)
                val result = countPossible(towels, restDesign)
                cache[restDesign] = result
                total += result
            }
        }
        return total
    }

    override fun part2(): Long {
        val towels = lines.first().split(", ")
        println(towels)
        println()
        var total = 0L
        for (design in lines.drop(2)) {
            cache.clear()
            println(design)
            val t = countPossible(towels, design)
            println(t)
            total += t
        }
        return total
    }
}
