package io.github.ocirne.aoc.year2019

import kotlin.math.pow

class IntCodeEmulator2019(val program: MutableMap<Long, Long>, noun: Long? = null, verb: Long? = null) {

    constructor(programStr: String): this(deserializeProgram(programStr))

    constructor(programStr: String, noun: Long? = null, verb: Long? = null): this(deserializeProgram(programStr), noun, verb)

    init {
        if (noun != null) program[1] = noun
        if (verb != null) program[2] = verb
    }

    // program pointer
    private var pp = 0L

    private var base = 0L

    private var inputList = mutableListOf<Long>()

    private var output = mutableListOf<Long>()

    fun copy(): IntCodeEmulator2019 {
        val copy = IntCodeEmulator2019(program.toMutableMap())
        copy.pp = pp
        copy.base = base
        copy.inputList = inputList.toMutableList()
        copy.output = output.toMutableList()
        return copy
    }

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
        while (tick() != ReturnCode.STOP) { /* */ }
        return this
    }

    /** runs the emulation until the next generated output */
    fun tick(): ReturnCode {
        while (true) {
            when (val opcode = currentOpcode()) {
                STOP -> return ReturnCode.STOP
                ADD -> mathInstruction { v1, v2 -> v1 + v2 }
                MUL -> mathInstruction { v1, v2 -> v1 * v2 }
                INPUT -> {
                    if (inputList.isEmpty()) {
                        return ReturnCode.NEED_INPUT
                    }
                    ioInstruction(immediate = true) { program[it] = inputList.removeFirst() }
                }
                OUTPUT -> {
                    ioInstruction(immediate = false) { output.add(it) }
                    return ReturnCode.HAS_OUTPUT
                }
                JMP_TRUE -> jumpInstruction { it != 0L }
                JMP_FALSE -> jumpInstruction { it == 0L }
                LESS_THAN -> mathInstruction { v1, v2 -> if (v1 < v2) 1 else 0 }
                EQUALS -> mathInstruction { v1, v2 -> if (v1 == v2) 1 else 0 }
                ADJUST_BASE -> ioInstruction(immediate = false) { base += it }
                else -> throw IllegalArgumentException("unknown opcode $opcode (pp: $pp)")
            }
        }
    }

    private fun getNextOutput(): Long? {
        if (tick() == ReturnCode.STOP) {
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

    fun joinCollectedOutput(): String {
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

        enum class ReturnCode {
            NEED_INPUT,
            HAS_OUTPUT,
            STOP
        }

        private fun deserializeProgram(programStr: String): MutableMap<Long, Long> {
            return programStr.split(',')
                .mapIndexed { index, value -> index.toLong() to value.toLong() }
                .toMap().toMutableMap()
        }
    }
}
