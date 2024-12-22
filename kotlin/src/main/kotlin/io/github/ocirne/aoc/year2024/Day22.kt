package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day22(val lines: List<String>) : AocChallenge(2024, 22) {

    private fun evolveNumber(x0: Long): Long {
        val x1 = ((x0 * 64) xor x0).mod(16777216L)
        val x2 = ((x1 / 32) xor x1).mod(16777216L)
        val x3 = ((x2 * 2048) xor x2).mod(16777216L)
        return x3
    }

    fun foo(x: Long): Long {
        var sn = x
        repeat(2000) { sn = evolveNumber(sn) }
        return sn
    }

    override fun part1(): Long {
        var total = 0L
        for (line in lines) {
            val x = foo(line.toLong())
            println(x)
            total += x
        }
        return total
    }

    override fun part2(): Int {
        return -1
    }
}
