package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.year2015.permutations

class Day7(val lines: List<String>) : AocChallenge(2019, 7) {

    fun amplifierChain(program: String, vararg inputs: Int): Int {
        var t = 0
        // TODO Reduce?
        inputs.forEach { i ->
            IntCodeEmulator2019(program).run(i, t).getDiagnosticCode().also { t = it }
        }
        return t
    }

    override fun part1(): Int {
        val inputs = listOf(0, 1,2, 3, 4)
        return inputs.permutations().map { p ->
            amplifierChain(lines.first(), *p.toIntArray())
        }.max()
    }

    override fun part2(): Int {
        TODO()
    }
}
