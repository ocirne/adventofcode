package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day8(val lines: List<String>) : AocChallenge(2019, 8) {

    private val BLACK = '0'
    private val WHITE = '1'
    private val TRANSPARENT = '2'

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

    override fun part2(): String {
        val width = 25
        val height = 6
        val layerSize = width * height
        val imageData = lines.first()
        val layers = imageData.chunked(layerSize)
        val finalImage = MutableList(layerSize) { TRANSPARENT }
        layers.forEach { layer ->
            layer.mapIndexed { i, c ->
                if (finalImage[i] == TRANSPARENT && layer[i] != TRANSPARENT) {
                    finalImage[i] = c
                }
            }
        }
        finalImage.chunked(width).forEach { line ->
            println(line.map { if (it == WHITE) '#' else ' ' }.joinToString(""))
        }
        return "."
    }
}
