package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge
import java.util.PriorityQueue

class Day17(val lines: List<String>) : AocChallenge(2023, 17) {

    fun readData(): Array<IntArray> {
        return lines.map { line -> line.map { c -> c.digitToInt() }.toIntArray() }.toTypedArray()
    }

    fun aStar(heatBlocks: Array<IntArray>): Int {
        val start = (0, 0, a)
        val openHeap = PriorityQueue()
        while
        return -1
    }

    override fun part1(): Int {
        val heatBlocks = readData()
        return aStar(heatBlocks)
    }

    override fun part2(): Int {
        return -1
    }
}
