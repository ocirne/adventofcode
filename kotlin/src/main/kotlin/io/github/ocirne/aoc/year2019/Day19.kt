package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day19(val lines: List<String>) : AocChallenge(2019, 19) {

    override fun part1(): Int {
        var total = 0
        for (y in 0L .. 49L) {
            for (x in 0L .. 49L) {
                val program = IntCodeEmulator2019(lines.first())
                program.addInput(x)
                program.addInput(y)
                program.tick()
                val c = program.getLastOutput().toInt()
                print(if (c == 1) '#' else '.')
                if (c == 1) total ++
            }
            println()
        }
        return total
    }

    override fun part2(): Int {
        return -1
    }
}
