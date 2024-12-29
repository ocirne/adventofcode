package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day22(val lines: List<String>) : AocChallenge(2024, 22) {

    private val modulo = 16777216L

    private fun evolveNumber(x0: Long): Long {
        val x1 = (x0 shl 6 xor x0).mod(modulo)
        val x2 = (x1 shr 5 xor x1).mod(modulo)
        return (x2 shl 11 xor x2).mod(modulo)
    }

    private fun secretNumbers(initialValue: Long): Sequence<Long> {
        return sequence {
            var sn = initialValue
            repeat(2001) {
                yield(sn)
                sn = evolveNumber(sn)
            }
        }
    }

    override fun part1(): Long {
        return lines.sumOf { line -> secretNumbers(line.toLong()).last() }
    }

    private fun deltaSecretNumbers(initialValue: Long): Sequence<Pair<Int, Int>> {
        return secretNumbers(initialValue)
            .map { it.mod(10) }
            .zipWithNext { a, b -> b - a to b }
    }

    fun changesToValue(initialValue: Long): Sequence<Pair<String, Int>> {
        return sequence {
            val queue = mutableListOf<Int>()
            for ((delta, value) in deltaSecretNumbers(initialValue)) {
                queue.add(delta)
                if (queue.size == 4) {
                    val key = queue.joinToString(",")
                    yield( key to value)
                    queue.removeFirst()
                }
            }
        }
    }

    private fun firstOccurrence(initialValue: Long): Map<String, Int> {
        val localBest = mutableMapOf<String, Int>()
        changesToValue(initialValue).forEach { (key, value) ->
            localBest.putIfAbsent(key, value)
        }
        return localBest
    }

    override fun part2(): Int {
        val totalMap = mutableMapOf<String, Int>()
        lines.forEach { line ->
            firstOccurrence(line.toLong()).forEach { (key, value) ->
                totalMap.compute(key) { _, e -> if (e != null) e + value else value }
            }
        }
        return totalMap.values.max()
    }
}
