package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day10(val lines: List<String>) : AocChallenge(2015, 10) {

    override fun part1(): Int {
        return playLookAndSay(40)
    }

    override fun part2(): Int {
        return playLookAndSay(50)
    }

    private fun playLookAndSay(rounds: Int): Int {
        var seq = lines.first().toList()
        repeat(rounds) { seq = step(seq) }
        return seq.size
    }

    fun step(seq: List<Char>): List<Char> {
        val result = ArrayList<Char>()
        var count = 0
        var lc = seq.first()
        seq.forEach { c ->
            if (c == lc) {
                count++
            } else {
                add(result, count, lc)
                count = 1
                lc = c
            }
        }
        add(result, count, lc)
        return result
    }

    private fun add(result: ArrayList<Char>, count: Int, lastCharacter: Char) {
        result.addAll(count.toString().toList())
        result.add(lastCharacter)
    }
}