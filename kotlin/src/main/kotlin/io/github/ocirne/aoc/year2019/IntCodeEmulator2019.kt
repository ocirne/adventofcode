package io.github.ocirne.aoc.year2019

import kotlin.math.pow

class IntCodeEmulator2019(programStr: String) {

    val program = programStr.split(',').map { it.toInt() }.toMutableList()

    // program pointer
    private var pp = 0

    private val output = mutableListOf<Int>()

    private fun paramMode(position: Int): Int {
        val b = 10.0.pow(position + 1).toInt()
        return (program[pp] / b) % 10
    }

    private fun getParameter(d: Int, immediate: Boolean=false): Int {
        val op = program[pp+d]
        return if (immediate || paramMode(d) == 1) op else program[op]
    }

    private fun mathInstruction(operation: (Int, Int) -> Int) {
        val p1 = getParameter(1)
        val p2 = getParameter(2)
        val p3 = getParameter(3, immediate = true)
        assert(paramMode(3) != 1)
        program[p3] = operation(p1, p2)
        pp += 4
    }

    private fun ioInstruction(immediate: Boolean, operation: (Int) -> Unit) {
        val p1 = getParameter(1, immediate = immediate)
        operation(p1)
        pp += 2
    }

    private fun jumpInstruction(evaluation: (Int) -> Boolean) {
        val p1 = getParameter(1)
        val p2 = getParameter(2)
        pp = if (evaluation(p1)) p2 else pp + 3
    }

    fun run(vararg inputs: Int, noun: Int? = null, verb: Int? = null): IntCodeEmulator2019 {
        if (noun != null) program[1] = noun
        if (verb != null) program[2] = verb
        val inputList = inputs.toMutableList()
        while (true) {
            when (val opcode = program[pp] % 100) {
                STOP -> return this
                ADD -> mathInstruction { v1, v2 -> v1 + v2 }
                MUL -> mathInstruction { v1, v2 -> v1 * v2 }
                INPUT -> ioInstruction(immediate = true) { program[it] = inputList.removeFirst() }
                OUTPUT -> ioInstruction(immediate = false) { output.add(it) }
                JMP_TRUE -> jumpInstruction { it != 0 }
                JMP_FALSE -> jumpInstruction { it == 0 }
                LESS_THAN -> mathInstruction { v1, v2 -> if (v1 < v2) 1 else 0 }
                EQUALS -> mathInstruction { v1, v2 -> if (v1 == v2) 1 else 0 }
                else -> throw IllegalArgumentException("unknown opcode $opcode (pp: $pp)")
            }
        }
    }

    fun getDiagnosticCode(): Int {
        return output.last()
    }

    override fun toString(): String {
        return program.joinToString(",") { it.toString() }
    }

    companion object {
        const val STOP = 99
        const val ADD = 1
        const val MUL = 2
        const val INPUT = 3
        const val OUTPUT = 4
        const val JMP_TRUE = 5
        const val JMP_FALSE = 6
        const val LESS_THAN = 7
        const val EQUALS = 8
    }
}
