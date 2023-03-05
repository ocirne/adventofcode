package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

const val STOP = 99
const val ADD = 1
const val MUL = 2

class IntCodeEmulatorDay2(programStr: String) {

    private val program = programStr.split(',').map { it.toInt() }.toMutableList()

    private var pp = 0
    private fun foo(operation: (Int, Int) -> Int) {
        val (op1, op2, tgt) = program.slice(pp + 1..pp + 3)
        program[tgt] = operation(program[op1], program[op2])
        pp += 4
    }

    fun run(verb: Int? = null, noun: Int? = null): IntCodeEmulatorDay2 {
        if (verb != null) program[1] = verb
        if (noun != null) program[2] = noun
        while (true) {
            when (val opcode = program[pp]) {
                STOP -> return this
                ADD -> foo { x, y -> x + y }
                MUL -> foo { x, y -> x * y }
                else -> throw IllegalArgumentException("unknown opcode $opcode")
            }
        }
    }

    fun getResult(): Int {
        return program[0]
    }

    override fun toString(): String {
        return program.joinToString(",") { it.toString() }
    }
}

class Day2(val lines: List<String>) : AocChallenge(2019, 2) {

    override fun part1(): Int {
        return IntCodeEmulatorDay2(lines.first()).run(12, 2).getResult()
    }

    override fun part2(): Int {
        val target = 19690720
        for (noun in 0..99) {
            for (verb in 0..99) {
                if (IntCodeEmulatorDay2(lines.first()).run(noun, verb).getResult() == target) {
                    return 100 * noun + verb
                }
            }
        }
        throw IllegalStateException("unreachable")
    }
}
