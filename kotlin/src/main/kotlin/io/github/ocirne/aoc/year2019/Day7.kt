package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.permutations

class Day7(val lines: List<String>) : AocChallenge(2019, 7) {

    fun amplifierChain(program: String, phaseSettings: List<Int>): Int {
        val amplifiers = phaseSettings.map { IntCodeEmulator2019(program).addInput(it) }
        var t = 0
        while (true) {
            for (amp in amplifiers) {
                amp.addInput(t)
                val done = amp.step()
                if (done) {
                    return amplifiers.last().getLastOutput()
                }
                t = amp.getLastOutput()
            }
        }
    }

    private fun maximumForPhaseSettings(vararg phaseSettings: Int): Int {
        return phaseSettings.toList()
            .permutations()
            .maxOf { amplifierChain(lines.first(), it) }
    }

    override fun part1(): Int {
        return maximumForPhaseSettings(0, 1, 2, 3, 4)
    }

    override fun part2(): Int {
        return maximumForPhaseSettings(5, 6, 7, 8, 9)
    }
}
