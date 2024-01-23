package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day19(val lines: List<String>) : AocChallenge(2019, 19) {

    private val m = 10_000L

    private fun beamOracle(x: Long, y: Long): Int {
        val program = IntCodeEmulator2019(lines.first())
        program.addInput(x)
        program.addInput(y)
        program.tick()
        return program.getLastOutput().toInt()
    }

    override fun part1(): Int {
        return LongRange(0L, 49L).sumOf { x ->
            LongRange(0L, 49L).sumOf { y ->
                beamOracle(x, y)
            }
        }
    }

    private fun checkResult(x: Long, y: Long): Boolean {
        return beamOracle(x+99, y) == 1 && beamOracle(x+100, y) == 0 &&
                beamOracle(x, y+99) == 1 && beamOracle(x, y+100) == 0
    }

    private fun findParameters(): List<Long> {
        return sequence {
            var inBeam = false
            for (y in 0L..m) {
                val c = beamOracle(m, y)
                if (inBeam) {
                    if (c == 0) {
                        yield(y - 1)
                        break
                    }
                } else {
                    if (c == 1) {
                        yield(y)
                        inBeam = true
                    }
                }
            }
        }.take(2).toList()
    }

    private fun findSuitableSpots(cx: Long, cy: Long): Sequence<Long> {
        return sequence {
            for (x in cx - 5..cx + 5) {
                for (y in cy - 5..cy + 5) {
                    if (checkResult(x, y)) {
                        yield(x * m + y)
                    }
                }
            }
        }
    }

    override fun part2(): Long {
        val (a, b) = findParameters()
        val cx = 99 * (m + a) / ( b - a)
        val cy = a * (cx + 99) / m
        return findSuitableSpots(cx, cy).min()
    }
}
