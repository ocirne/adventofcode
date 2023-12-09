package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.max
import kotlin.math.min

class Day5(val lines: List<String>) : AocChallenge(2023, 5) {

    data class UseType(val start: Long, val end: Long, val delta: Long)

    private val seeds = if (lines.isEmpty()) {
        listOf()
    } else {
        lines.first().split(":").last().trim().split(" ").map { it.toLong() }
    }

    class Almanac(val lines: List<String>) {

        private val almanac = addMissingRanges(readAlmanac(lines))

        private fun readAlmanac(lines: List<String>): List<List<UseType>> {
            if (lines.isEmpty()) {
                return listOf()
            }
            val rawAlmanac = mutableListOf<List<UseType>>()
            var useTypes = mutableListOf<UseType>()
            for (line in lines.drop(1)) {
                when {
                    line.isBlank() -> {
                        if (useTypes.isNotEmpty()) {
                            rawAlmanac.add(useTypes)
                        }
                        useTypes = mutableListOf()
                    }

                    line.endsWith(':') -> {
                        // ignore
                    }

                    else -> {
                        val (destinationStart, sourceStart, rangeLength)
                                = line.split(' ').map { it.toLong() }
                        val sourceEnd = sourceStart + rangeLength
                        val delta = destinationStart - sourceStart
                        useTypes.add(UseType(sourceStart, sourceEnd, delta))
                    }
                }
            }
            rawAlmanac.add(useTypes)
            return rawAlmanac
        }

        private fun addMissingRanges(rawAlmanac: List<List<UseType>>): List<List<UseType>> {
            return rawAlmanac.map { useTypes ->
                val t = useTypes.sortedBy { it.start }
                val useType = mutableListOf(t.first())
                t.zipWithNext { a, b ->
                    if (a.end < b.start) {
                        useType.add(UseType(a.end, b.start, 0))
                    }
                    useType.add(b)
                }
                listOf(UseType(Long.MIN_VALUE, t.first().start, 0)) +
                        useType.toList() +
                        listOf(UseType(t.last().end, Long.MAX_VALUE, 0))
            }
        }

        fun findLocation(start: Long, end: Long, depth: Int = 0): Long {
            if (depth >= almanac.size) {
                return start
            }
            return almanac[depth].filter { useType ->
                start < useType.end && useType.start < end
            }.minOfOrNull { useType ->
                findLocation(
                    start = max(start + useType.delta, useType.start + useType.delta),
                    end = min(end + useType.delta, useType.end + useType.delta),
                    depth = depth + 1,
                )
            } ?: Long.MAX_VALUE
        }
    }

    private val almanac = Almanac(lines)

    override fun part1(): Long {
        return seeds.minOf { seed ->
            almanac.findLocation(seed, seed + 1)
        }
    }

    override fun part2(): Long {
        return seeds.chunked(2).minOf { (start, length) ->
            almanac.findLocation(start, start + length)
        }
    }
}
