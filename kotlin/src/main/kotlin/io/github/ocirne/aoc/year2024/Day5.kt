package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day5(val lines: List<String>) : AocChallenge(2024, 5) {

    private fun isValid(rules: Set<Pair<String, String>>, numbers: String): Boolean {
        rules.forEach { (p1, p2) ->
            val f1 = numbers.indexOf(p1)
            val f2 = numbers.indexOf(p2)
            if (f1 != -1 && f2 != -1 && f1 > f2) {
                return false
            }
        }
        return true
    }

    class RulesComparator(private val rules: Set<Pair<String, String>>) : Comparator<String> {
        override fun compare(a: String, b: String): Int {
            return when {
                rules.contains(Pair(a, b)) -> -1
                rules.contains(Pair(b, a)) -> 1
                else -> 0
            }
        }
    }

    private fun readRules(): Set<Pair<String, String>> {
        return lines.takeWhile { it.isNotBlank() }.map { line ->
            val (r1, r2) = line.trim().split('|')
            Pair(r1, r2)
        }.toSet()
    }

    private fun readNumbers(): List<String> {
        return lines.dropWhile { it.isNotBlank() }.drop(1)
    }

    private fun middlePageNumber(values: List<String>): Int {
        return values[values.size / 2].toInt()
    }

    override fun part1(): Int {
        val rules = readRules()
        return readNumbers()
            .filter { isValid(rules, it) }
            .map { it.split(',') }
            .sumOf { middlePageNumber(it) }
    }

    override fun part2(): Int {
        val rules = readRules()
        val rulesComparator = RulesComparator(rules)
        return readNumbers()
            .filter { !isValid(rules, it) }
            .map { it.split(',') }
            .map { it.sortedWith(rulesComparator) }
            .sumOf { middlePageNumber(it) }
    }
}
