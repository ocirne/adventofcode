package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day17(val lines: List<String>) : AocChallenge(2019, 17) {

    private fun runProgram(): Map<Pair<Long, Long>, Char> {
        val program = IntCodeEmulator2019(lines.first())
        val cameraOutput = mutableMapOf<Pair<Long, Long>, Char>()
        var x = 0L
        var y = 0L
        while (program.tick() != IntCodeEmulator2019.Companion.ReturnCode.STOP) {
            val c = program.getLastOutput().toInt()
            if (c == 10) {
                y += 1
                x = 0
            } else {
                if (c == 35) {
                    cameraOutput[x to y] = c.toChar()
                }
                x += 1
            }
        }
        return cameraOutput
    }

    fun foo(cameraOutput: Map<Pair<Long, Long>, Char>): Long {
        return cameraOutput.filterKeys { (x, y) ->
            cameraOutput[x - 1 to y] == '#' &&
                    cameraOutput[x + 1 to y] == '#' &&
                    cameraOutput[x to y - 1] == '#' &&
                    cameraOutput[x to y + 1] == '#'
        }.keys.sumOf { (x, y) -> x * y }
    }

    override fun part1(): Long {
        val cameraOutput = runProgram()
        return foo(cameraOutput)
    }

    override fun part2(): Int {
        return -1
    }
}
