package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.abs

fun List<Int>.withoutIndex(index: Int): List<Int> = this.subList(0, index)  + this.subList(index + 1, this.size)

class Day2(val lines: List<String>) : AocChallenge(2024, 2) {

    private fun isSafeDeltas(deltas: List<Int>): Boolean {
        return (deltas.all { it > 0 } || deltas.all { it < 0 }) && deltas.all { abs(it) < 4}
    }

    private fun isSafe(line: String, withDampener: Boolean = false): Boolean {
        val values = line.split(' ').map(String::toInt)
        val deltas = values.zipWithNext().map { (x, y) -> y - x }
        if (isSafeDeltas(deltas)) {
            return true
        }
        if (!withDampener) {
            return false
        }
        for (i in values.indices) {
            val subDeltas = values.withoutIndex(i).zipWithNext().map { (x, y) -> y - x }
            if (isSafeDeltas(subDeltas)) {
                return true
            }
        }
        return false
    }

    override fun part1(): Int {
        return lines.count(::isSafe)
    }

    override fun part2(): Int {
        return lines.count { line -> isSafe(line, withDampener = true) }
    }
}
