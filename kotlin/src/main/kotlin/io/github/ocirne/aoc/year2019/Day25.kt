package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day25(val lines: List<String>) : AocChallenge(2019, 25) {

    private fun runProgram(program: IntCodeEmulator2019): Long {
        while (true) {
            val rc = program.tick()
            when (rc) {
                IntCodeEmulator2019.Companion.ReturnCode.NEED_INPUT -> {
                    val stringInput = readln()
                    stringInput.forEach { program.addInput(it.code.toLong()) }
                    program.addInput(10)
                }
                IntCodeEmulator2019.Companion.ReturnCode.HAS_OUTPUT -> {
                    print(program.getLastOutput().toInt().toChar())
                }
                IntCodeEmulator2019.Companion.ReturnCode.STOP -> {
                    break
                }
            }
        }
        return -1
    }

    override fun part1(): Long {
        val program = IntCodeEmulator2019(lines.first())
        return runProgram(program)
    }

    override fun part2() {}
}
