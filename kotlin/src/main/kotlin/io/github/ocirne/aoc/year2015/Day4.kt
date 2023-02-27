package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge
import java.math.BigInteger
import java.security.MessageDigest

class Day4(val lines: List<String>) : AocChallenge(2015, 4) {

    private val md = MessageDigest.getInstance("MD5")

    private fun check(s: String, length: Int): Boolean {
        val bytes = md.digest(s.toByteArray())
        return BigInteger(1, bytes).toString(16).length > length
    }

    fun search(base: String, zeros: Int): Int {
        return generateSequence(1, Int::inc)
            .dropWhile { i -> check(base + i.toString(), 32 - zeros) }
            .first()
    }

    override fun part1(): Int {
        return search(lines.first(), 5)
    }

    override fun part2(): Int {
        return search(lines.first(), 6)
    }
}
