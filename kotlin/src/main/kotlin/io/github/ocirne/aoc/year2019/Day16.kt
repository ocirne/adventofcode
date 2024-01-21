package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.absoluteValue

class Day16(val lines: List<String>) : AocChallenge(2019, 16) {

    fun basePattern(x: Int, y: Int): Int {
        return listOf(0, 1, 0, -1)[(x+1) / y % 4]
    }

    fun newSignal(signal: List<Int>): List<Int> {
        return IntRange(1, signal.size).map { y ->
            signal.mapIndexed { x, value2 ->
                basePattern(x, y) * value2
            }.sum().absoluteValue % 10
        }
    }

    fun foo(signalString: String, phases: Int=100): String {
        var signal = signalString.toCharArray().map { it.digitToInt() }
        repeat(phases) {
            signal = newSignal(signal)
        }
        return signal.take(8).joinToString("")
    }

    override fun part1(): String {
        return foo(lines.first())
    }
    
    fun foo2(signalString: String, phases: Int=100): String {
        val skip = signalString.take(7).toInt()
        val signal = signalString.repeat(10000).toCharArray().drop(skip).map { it.digitToInt() }.reversed().toIntArray()
        repeat(100) {
            var s = 0
            for (i in 0 until signal.size) {
                s += signal[i]
                signal[i] = s % 10
            }
        }
        return signal.reversed().take(8).joinToString("")
    }

    override fun part2(): String {
        return foo2(lines.first())
    }
}
