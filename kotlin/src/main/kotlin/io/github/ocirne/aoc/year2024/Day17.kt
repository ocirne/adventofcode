package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.hypot

class Day17(val lines: List<String>) : AocChallenge(2024, 17) {

    private fun findComboOperand(operand: Long, a: Long, b: Long, c: Long) : Long {
        return when (operand) {
            4L -> a
            5L -> b
            6L -> c
            7L -> throw IllegalStateException()
            else -> operand
        }
    }

    private val adv = 0L
    private val bxl = 1L
    private val bst = 2L
    private val jnz = 3L
    private val bxc = 4L
    private val out = 5L
    private val bdv = 6L
    private val cdv = 7L

    private fun runProgram(programStr: String, initialA: Long, initialB: Long, initialC: Long): String {
        var a = initialA
        var b = initialB
        var c = initialC
        val program = programStr.split(',').map { it.toLong() }
        var ip = 0
        val output = mutableListOf<String>()
        while (true) {
            if (ip < 0 || ip > program.size - 1) {
                return output.joinToString(",")
            }
            val opcode = program[ip]
            val literalOperand = program[ip+1]
            val comboOperand = findComboOperand(literalOperand, a, b, c)
            when (opcode) {
                adv -> a = a shr comboOperand.toInt()
                bxl -> b = b xor literalOperand
                bst -> b = comboOperand and 7
                jnz -> if (a != 0L) ip = (literalOperand - 2L).toInt()
                bxc -> b = b xor c
                out -> output.add((comboOperand and 7).toString())
                bdv -> b = a shr comboOperand.toInt()
                cdv -> c = a shr comboOperand.toInt()
            }
            ip += 2
        }
    }

    override fun part1(): String {
        val a = lines[0].split(": ").last().toLong()
        val b = lines[1].split(": ").last().toLong()
        val c = lines[2].split(": ").last().toLong()
        val program = lines[4].split(": ").last()
        return runProgram(program, a, b, c)
    }

/*    0 000  011 011  3  11-0
    1 001  011 010  2  11-1
    2 010  011 001  1  11-2
    3 011  011 000  0  11-3
    4 100  011 111  7  11-4
    5 101  011 110  6  11-5
    6 110  011 101  5  11-6
    7 111  011 100  4  11-7
*/

/*  0 000  101  101  5
    1 001  101  100  4
    2 010  101  111  7
    3 011  101  110  6
    4 100  101  001  1
    5 101  101  000  0
    6 110  101  011  3
    7 111  101  010  2
*/

    fun part2_hardcoded(initialA: Long): String {
        val output = mutableListOf<Long>()
        var a = initialA
        var b = 0L
        var c = 0L
        do {
            b = a.mod(8L)
            b = b xor 3L
            c = a shr b.toInt()
            a = a shr 3
            b = b xor 5L
            b = b xor c
            output.add(b.mod(8L)).toString()
        } while (a != 0L)
        return output.map { it.toString() }.joinToString(",")
    }

    fun part2_hardcoded_test(initialA: Long): String {
        val output = mutableListOf<Long>()
        var a = initialA
        var b = 0L
        var c = 0L
        do {
            a = a shr 3
            output.add(a % 8).toString()
        } while (a != 0L)
        return output.map { it.toString() }.joinToString(",")
    }

    fun step(inA: Long): Long {
        var a = inA
        var b = a % 8L
        b = b xor 3L
        val c = a shr b.toInt()
        a = a shr 3
        b = b xor 5L
        b = b xor c
        val o = b % 8
        return o
    }

    fun step_test(inA: Long): Long {
        var a = inA
//        a = a shr 3
        val o = a % 8
        return o
    }

    fun part2_hardcoded2_rec(programStr: String, d: Int = 0, agg: Long=0): Long? {
        if (d == 0) {
            return agg
        }
        println("" + agg + " " + (agg / 8L))
//        val m = if (d == 16) 10000L else 7L
        for (a in 0L..7L) {
            val agg2 = agg or a
//            println(agg2)
//            agg2 = agg2 shl 3
            val o = part2_hardcoded(agg2)
            if (programStr == o) {
                return agg2
            }
            if (programStr.endsWith(o)) {
                println("d $d, a $a, o $o -- $programStr")
                val t = part2_hardcoded2_rec(programStr, d-1, agg2 shl 3)
                if (t != null) {
                    return t
                }
            }
        }
        return null
    }

    override fun part2(): Long {
        //r a = 35185000000000L
        var a = 35184370000000L
        val program = lines[4].split(": ").last()
        val size = program.split(',').size
        val r = part2_hardcoded2_rec(program, size)
        if (r != null) {
            println("r " + r)
            println("test " + part2_hardcoded(r))
        }
//        println("ref1 " + part2_hardcoded(117440))
        println("ref2 " + program + " (really)")
        return -1
    }
}
