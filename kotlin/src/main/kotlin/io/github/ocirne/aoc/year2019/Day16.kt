package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.absoluteValue

class Day16(val lines: List<String>) : AocChallenge(2019, 16) {

    private val basePattern = arrayOf(0, 1, 0, -1)

    private fun nextSignal(signal: IntArray): IntArray {
        return IntRange(1, signal.size).map { y ->
            signal.mapIndexed { x, value ->
                basePattern[(x+1) / y % 4] * value
            }.sum().absoluteValue % 10
        }.toIntArray()
    }

    fun naive(signalString: String, phases: Int=100): String {
        var signal = signalString.map { it.digitToInt() }.toIntArray()
        repeat(phases) {
            signal = nextSignal(signal)
        }
        return signal.take(8).joinToString("")
    }

    override fun part1(): String {
        return naive(lines.first())
    }

    override fun part2(): String {
        val signalString = lines.first()
        val skip = signalString.take(7).toInt()
        val signal = signalString.repeat(10000).drop(skip).map { it.digitToInt() }.toIntArray()
        repeat(100) {
            (signal.size-2 downTo 0).forEach { i ->
                signal[i] = (signal[i] + signal[i+1]) % 10
            }
        }
        return signal.take(8).joinToString("")
    }
}
