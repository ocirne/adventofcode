package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

const val STOP = 99
const val ADD = 1
const val MUL = 2

class Day2(val lines: List<String>) : AocChallenge(2019, 2) {

    fun runProgram(programStr: String, verb: Int=12, noun: Int=2): Int {
        println(programStr)
        println(programStr.split(','))
        val program = programStr.split(',').map { it.toInt() }.toMutableList()
        println(program)
        program[1] = verb
        program[2] = noun

        var p = 0
        while (true) {
            val opcode = program[p]
            when (opcode) {
                STOP -> {
                    return program[0]
//                    return program.joinToString(",") { it.toString() }
                }
                ADD -> {
                    program[program[p + 3]] = program[program[p + 1]] + program[program[p + 2]]
                    p += 4
                }
                MUL -> {
                    program[program[p + 3]] = program[program[p + 1]] * program[program[p + 2]]
                    p += 4
                }
                else -> {
                    throw RuntimeException(opcode.toString())
                }
            }
        }
    }

    override fun part1(): Int {
        return runProgram(lines.first())
    }

    override fun part2(): Int {
        val target = 19690720
        for (noun in 0 .. 99) {
            for (verb in 0 .. 99) {
                if (runProgram(lines.first(), noun, verb) == target) {
                    return 100 * noun + verb
                }
            }
        }
        throw IllegalStateException("unreachable")
    }
}
