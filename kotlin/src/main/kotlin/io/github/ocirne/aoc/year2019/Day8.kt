package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day8(val lines: List<String>) : AocChallenge(2019, 8) {

    private fun countDigit(layer: String, digit: Char): Int {
        return layer.count { c -> c == digit }
    }

    fun checkUncorrupted(width: Int, height: Int): Int {
        val imageData = lines.first()
        val layers = imageData.chunked(width * height)
        val layer = layers.minByOrNull { layer -> countDigit(layer, '0') }!!
        val ones = countDigit(layer, '1')
        val twos = countDigit(layer, '2')
        return ones * twos
    }

    override fun part1(): Int {
        return checkUncorrupted(25, 6)
    }

    override fun part2(): Int {
        return -1
    }
}
