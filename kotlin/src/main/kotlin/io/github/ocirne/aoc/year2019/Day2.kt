package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day2(val lines: List<String>) : AocChallenge(2019, 2) {

    override fun part1(): Long {
        return IntCodeEmulator2019(lines.first(), noun = 12, verb = 2).run().program[0]!!
    }

    override fun part2(): Long {
        val target = 19690720L
        for (noun in 0..99L) {
            for (verb in 0..99L) {
                if (IntCodeEmulator2019(lines.first(), noun = noun, verb = verb).run().program[0] == target) {
                    return 100L * noun + verb
                }
            }
        }
        throw IllegalStateException("unreachable")
    }
}
