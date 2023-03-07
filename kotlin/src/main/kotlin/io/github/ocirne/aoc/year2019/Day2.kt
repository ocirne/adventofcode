package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day2(val lines: List<String>) : AocChallenge(2019, 2) {

    override fun part1(): Int {
        return IntCodeEmulator2019(lines.first(), noun = 12, verb = 2).run().program.first()
    }

    override fun part2(): Int {
        val target = 19690720
        for (noun in 0..99) {
            for (verb in 0..99) {
                if (IntCodeEmulator2019(lines.first(), noun = noun, verb = verb).run().program.first() == target) {
                    return 100 * noun + verb
                }
            }
        }
        throw IllegalStateException("unreachable")
    }
}
