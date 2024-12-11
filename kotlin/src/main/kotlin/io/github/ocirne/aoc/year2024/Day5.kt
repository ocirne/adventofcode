package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day5(val lines: List<String>) : AocChallenge(2024, 5) {

    fun isValid(rules: List<Pair<String, String>>, numbers: String): Boolean {
        rules.forEach { (p1, p2) ->
            val f1 = numbers.indexOf(p1)
            val f2 = numbers.indexOf(p2)
            if (f1 != -1 && f2 != -1 && f1 > f2) {
                return false
            }
        }
        return true
    }

    override fun part1(): Int {
        val rules = mutableListOf<Pair<String, String>>()
        for (line in lines.takeWhile { it.isNotBlank() }) {
            val (r1, r2) = line.trim().split('|')
            rules.add(Pair(r1, r2))
        }
        var total = 0
        for (numbers in lines.dropWhile { it.isNotBlank() }.drop(1) ) {
            if (isValid(rules, numbers)) {
                val values = numbers.split(',')
                total += values[values.size / 2].toInt()
            }
        }
        return total
    }

    class RulesComparator(val rules: List<Pair<String, String>>) : Comparator<String> {
        override fun compare(string1: String, string2: String): Int {
            if (rules.contains(Pair(string1, string2))) {
                return -1
            }
            if (rules.contains(Pair(string2, string1))) {
                return 1
            }
            return 0
        }
    }

    override fun part2(): Int {
        val rules = mutableListOf<Pair<String, String>>()
        for (line in lines.takeWhile { it.isNotBlank() }) {
            val (r1, r2) = line.trim().split('|')
            rules.add(Pair(r1, r2))
        }
        val rulesComparator = RulesComparator(rules)
        var total = 0
        for (numbers in lines.dropWhile { it.isNotBlank() }.drop(1) ) {
            if (isValid(rules, numbers)) {
            } else {
                val values = numbers.split(',')
                val values2 = values.sortedWith(rulesComparator)
                total += values2[values2.size / 2].toInt()
            }
        }
        return total
    }
}
