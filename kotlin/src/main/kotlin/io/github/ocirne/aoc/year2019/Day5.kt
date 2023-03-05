package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.pow

const val INPUT = 3
const val OUTPUT = 4

class IntCodeEmulatorDay5(programStr: String) {

    private val program = programStr.split(',').map { it.toInt() }.toMutableList()

    private fun paramMode(position: Int): Boolean {
        val b = 10.0.pow(position + 1).toInt()
        return (program[pp] / b) % 10 == 1
    }

    // input pointer
    var ip = 0
    // program pointer
    var pp = 0

    val output = mutableListOf<Int>()

    fun run(inputs: List<Int>, verb: Int? = null, noun: Int? = null): IntCodeEmulatorDay5 {
        println("---- run " + toString() + " ----")
        if (verb != null) program[1] = verb
        if (noun != null) program[2] = noun
        while (true) {
            when (val opcode = program[pp] % 100) {
                STOP -> return this
                ADD -> {
                    val op1 = program[pp+1]
                    val op2 = program[pp+2]
                    val tgt = program[pp+3]
                    val v1 = if (paramMode(1)) op1 else program[op1]
                    val v2 = if (paramMode(2)) op2 else program[op2]
                    assert(!paramMode(3))
                    assert(tgt != pp)
                    println("add $tgt = $v1 + $v2")
                    program[tgt] = v1 + v2
                    pp += 4
                }
                MUL -> {
                    val op1 = program[pp+1]
                    val op2 = program[pp+2]
                    val tgt = program[pp+3]
                    val v1 = if (paramMode(1)) op1 else program[op1]
                    val v2 = if (paramMode(2)) op2 else program[op2]
                    assert(!paramMode(3))
                    assert(tgt != pp)
                    println("mul $tgt = $v1 * $v2")
                    program[tgt] = v1 * v2
                    pp += 4
                }
                INPUT -> {
                    val op1 = program[pp+1]
                    assert(!paramMode(1))
                    val v1 = op1
                    program[v1] = inputs[ip]
                    assert(v1 != pp)
                    println("input $v1 = " + inputs[ip])
                    ip++
                    pp += 2
                }
                OUTPUT -> {
                    val op1 = program[pp+1]
//                    assert(!paramMode(1))
                    val v1 = if (paramMode(1)) op1 else program[op1]
                    println("output += $v1")
                    output.add(v1)
                    pp += 2
                }
                // Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the
                // value from the second parameter. Otherwise, it does nothing.
                5 -> {
                    val op1 = program[pp+1]
                    val tgt = program[pp+2]
                    val v1 = if (paramMode(1)) op1 else program[op1]
                    val t1 = if (paramMode(2)) tgt else program[tgt]
                    if (v1 != 0) {
                        println("jump-if-true $v1 => $pp = $t1")
                        pp = t1
                    } else {
                        println("jump-if-true $v1 => nothing")
                        pp += 3
                    }
                }
                // Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the
                // value from the second parameter. Otherwise, it does nothing.
                6 -> {
                    val op1 = program[pp+1]
                    val tgt = program[pp+2]
                    val v1 = if (paramMode(1)) op1 else program[op1]
                    val t1 = if (paramMode(2)) tgt else program[tgt]
                    if (v1 == 0) {
                        println("jump-if-false $v1 => $pp = $t1")
                        pp = t1
                    } else {
                        println("jump-if-false $v1 => nothing")
                        pp += 3
                    }
                }
                // Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the
                // position given by the third parameter. Otherwise, it stores 0.
                7 -> {
                    val op1 = program[pp+1]
                    val op2 = program[pp+2]
                    val tgt = program[pp+3]
                    val v1 = if (paramMode(1)) op1 else program[op1]
                    val v2 = if (paramMode(2)) op2 else program[op2]
                    assert(!paramMode(3))
                    assert(tgt != pp)
                    println("less-than ($v1, $v2) => $tgt")
                    program[tgt] = if (v1 < v2) 1 else 0
                    pp += 4
                }
                // Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the
                // position given by the third parameter. Otherwise, it stores 0.
                8 -> {
                    val op1 = program[pp+1]
                    val op2 = program[pp+2]
                    val tgt = program[pp+3]
                    val v1 = if (paramMode(1)) op1 else program[op1]
                    val v2 = if (paramMode(2)) op2 else program[op2]
                    assert(!paramMode(3))
                    assert(tgt != pp)
                    println("equals ($v1, $v2) => $tgt")
                    program[tgt] = if (v1 == v2) 1 else 0
                    pp += 4
                }
                else -> throw IllegalArgumentException("unknown opcode $opcode (pp: $pp, ip $ip) - " + program[pp])
            }
        }
    }

    fun getDiagnosticCode(): Int {
        return output.last()
    }

    override fun toString(): String {
        return program.joinToString(",") { it.toString() }
    }
}

class Day5(val lines: List<String>) : AocChallenge(2019, 5) {

    override fun part1(): Int {
        return IntCodeEmulatorDay5(lines.first()).run(listOf(1)).getDiagnosticCode()
    }

    override fun part2(): Int {
        return IntCodeEmulatorDay5(lines.first()).run(listOf(5)).getDiagnosticCode()
    }
}
