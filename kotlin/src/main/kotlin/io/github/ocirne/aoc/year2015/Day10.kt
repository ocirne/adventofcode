package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day10(val lines: List<String>) : AocChallenge(2015, 10) {

    private val startSequence = lines.getOrNull(0)

    override fun part1(): Int {
        return playLookAndSay(40)
    }

    override fun part2(): Int {
        return playLookAndSay(50)
    }

    private fun playLookAndSay(rounds: Int): Int {
        var seq = startSequence!!
        repeat(rounds) {
            seq = step(seq) }
        return seq.length
    }

    fun step(seq: String):String {
        var result = ""
        var count = 0
        var lc = seq[0]
        seq.forEach { c ->
            if (c == lc) {
                count++
            } else {
                result += count.toString() + lc
                count = 1
                lc = c
            }
        }
        result += count.toString() + lc
        return result
    }
}