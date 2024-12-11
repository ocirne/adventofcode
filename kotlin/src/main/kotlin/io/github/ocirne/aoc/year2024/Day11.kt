package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.log10
import kotlin.math.pow

class Day11(val lines: List<String>) : AocChallenge(2024, 11) {

    class Blink(line: String) {

        private val startNumbers = line.trim().split(' ').map { it.toLong() }

        private val cache = mutableMapOf<Pair<Long, Int>, Long>()

        private fun recursiveBlink(x: Long, step: Int): Long {
            if (x to step in cache) {
                return cache[x to step]!!
            }
            if (step == 0) {
                return 1
            }
            val length = log10(x.toDouble()).toInt() + 1
            val result = when {
                x == 0L -> recursiveBlink(1, step - 1)
                length % 2 == 0 -> {
                    val m = (10.0).pow(length / 2).toInt()
                    recursiveBlink(x / m, step - 1) + recursiveBlink(x % m, step - 1)
                }
                else -> recursiveBlink(2024 * x, step - 1)
            }
            cache[x to step] = result
            return result
        }

        fun blinks(times: Int): Long {
            return startNumbers.sumOf { recursiveBlink(it, times) }
        }
    }

    override fun part1(): Long {
        return Blink(lines.first()).blinks(25)
    }

    override fun part2(): Long {
        return Blink(lines.first()).blinks(75)
    }
}
