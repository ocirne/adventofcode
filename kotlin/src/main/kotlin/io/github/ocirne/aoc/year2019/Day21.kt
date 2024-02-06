package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day21(val lines: List<String>) : AocChallenge(2019, 21) {

    private fun runProgram(program: IntCodeEmulator2019, print: Boolean=false): Long {
        while (true) {
            val rc = program.tick()
            if (rc == IntCodeEmulator2019.Companion.ReturnCode.STOP) {
                break
            }
            else if (rc == IntCodeEmulator2019.Companion.ReturnCode.NEED_INPUT) {
                break
            }
            else {
                val lo = program.getLastOutput()
                if (lo > 255) {
                    return lo
                }
                val c = lo.toInt().toChar()
                if (print) {
                    print("$c")
                }
            }
        }
        return -1
    }

    private fun runScript(script: String): Long {
        val program = IntCodeEmulator2019(lines.first())
        script.forEach { program.addInput(it.code.toLong()) }
        return runProgram(program)
    }

    override fun part1(): Long {
        val script = """
            NOT T T
            AND A T
            AND B T
            AND C T
            NOT T J
            AND D J
            WALK

        """.trimIndent()
        return runScript(script)
    }

    override fun part2(): Long {
        val script = """
            NOT T T
            AND B T
            AND C T
            NOT T T
            AND D T
            AND H T
            NOT A J
            OR T J
            RUN

        """.trimIndent()
        return runScript(script)
    }
}
