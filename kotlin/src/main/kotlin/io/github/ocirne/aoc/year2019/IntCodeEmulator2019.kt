package io.github.ocirne.aoc.year2019

import kotlin.math.pow

class IntCodeEmulator2019(programStr: String, noun: Long? = null, verb: Long? = null) {

    val program =
        programStr.split(',')
            .mapIndexed { index, value -> index.toLong() to value.toLong() }
            .toMap().toMutableMap()

    init {
        if (noun != null) program[1] = noun
        if (verb != null) program[2] = verb
    }

    // program pointer
    private var pp = 0L

    private var base = 0L

    private val inputList = mutableListOf<Long>()

    private val output = mutableListOf<Long>()

    private fun currentOpcode(): Int {
        return (program[pp]!! % 100).toInt()
    }

    private fun paramMode(position: Long): Long {
        val b = 10.0.pow(position + 1.0).toInt()
        return (program[pp]!! / b) % 10
    }

    private fun getParameter(d: Long, immediate: Boolean = false): Long {
        val pm = paramMode(d)
        val op = program[pp + d]!! + if (pm == 2L) base else 0
        return if (immediate || pm == 1L) op else program.getOrDefault(op, 0L)
    }

    private fun mathInstruction(operation: (Long, Long) -> Long) {
        val p1 = getParameter(1)
        val p2 = getParameter(2)
        val p3 = getParameter(3, immediate = true)
        assert(paramMode(3) != 1L)
        program[p3] = operation(p1, p2)
        pp += 4
    }

    private fun ioInstruction(immediate: Boolean, operation: (Long) -> Unit) {
        val p1 = getParameter(1, immediate = immediate)
        operation(p1)
        pp += 2
    }

    private fun jumpInstruction(evaluation: (Long) -> Boolean) {
        val p1 = getParameter(1)
        val p2 = getParameter(2)
        pp = if (evaluation(p1)) p2 else pp + 3
    }

    fun addInput(i: Long): IntCodeEmulator2019 {
        inputList.add(i)
        return this
    }

    fun run(vararg inputs: Long): IntCodeEmulator2019 {
        inputList.addAll(inputs.toList())
        while (!tick()) { /* */ }
        return this
    }

    /** runs the emulation until the next generated output */
    fun tick(): Boolean {
        while (true) {
            when (val opcode = currentOpcode()) {
                STOP -> return true
                ADD -> mathInstruction { v1, v2 -> v1 + v2 }
                MUL -> mathInstruction { v1, v2 -> v1 * v2 }
                INPUT -> ioInstruction(immediate = true) { program[it] = inputList.removeFirst() }
                OUTPUT -> { ioInstruction(immediate = false) { output.add(it) }; return false }
                JMP_TRUE -> jumpInstruction { it != 0L }
                JMP_FALSE -> jumpInstruction { it == 0L }
                LESS_THAN -> mathInstruction { v1, v2 -> if (v1 < v2) 1 else 0 }
                EQUALS -> mathInstruction { v1, v2 -> if (v1 == v2) 1 else 0 }
                ADJUST_BASE -> ioInstruction(immediate = false) { base += it }
                else -> throw IllegalArgumentException("unknown opcode $opcode (pp: $pp)")
            }
        }
    }

    fun getNextOutput(): Long? {
        if (tick()) {
            return null
        }
        return getLastOutput()
    }

    fun getNextOutputs(n: Int): List<Long>? {
        return IntRange(1, n).map { getNextOutput() ?: return null }
    }

    fun getLastOutput(): Long {
        return output.last()
    }

    fun getOutput(): String {
        return output.joinToString(",") { it.toString() }
    }

    override fun toString(): String {
        val m = program.keys.max()
        if (m > 1_000_000) {
            throw RuntimeException("programm too large")
        }
        return program.toSortedMap().values.joinToString(",") { it.toString() }
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
        const val ADJUST_BASE = 9
    }
}
