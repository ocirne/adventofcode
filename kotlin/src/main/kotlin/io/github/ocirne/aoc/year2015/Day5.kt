package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day5(val lines: List<String>) : AocChallenge(2015, 5) {

    override fun part1(): Int {
        return lines.count { s -> isNicePart1(s) }
    }

    override fun part2(): Int {
        return lines.count { s -> isNicePart2(s) }
    }

    fun isNicePart1(s: String): Boolean {
        return containsAtLeastThreeVowels(s) && containsDoubleLetter(s) && containsNoForbiddenString(s)
    }

    fun isNicePart2(s: String): Boolean {
        return containsDoublePair(s) && containsOneLetterBetween(s)
    }

    private fun containsAtLeastThreeVowels(s: String) : Boolean {
        return s.count { c -> "aeiou".contains(c) } >= 3
    }

    private fun containsDoubleLetter(s: String) : Boolean {
        return s.zipWithNext { a, b -> a == b }.any { it }
    }

    private fun containsNoForbiddenString(s: String) : Boolean {
        return FORBIDDEN.map { f -> s.contains(f) }.none { it }
    }

    private fun containsDoublePair(s: String) : Boolean {
        for (i in 0..s.length-2) {
            val pair = s.substring(i, i+2)
            val rest = s.substring(i+2)
            if (rest.contains(pair)) {
                return true
            }
        }
        return false
    }

    private fun containsOneLetterBetween(s: String) : Boolean {
        return s.zip(s.drop(2)).any { (a, b) -> a == b }
    }

    companion object {
        private val FORBIDDEN = "ab cd pq xy".split(' ')
    }
}
