package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

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

    override fun part1(): String {
        var a = lines[0].split(": ").last().toLong()
        var b = lines[1].split(": ").last().toLong()
        var c = lines[2].split(": ").last().toLong()
        val program = lines[4].split(": ").last().split(',').map { it.toLong() }
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
                bst -> b = comboOperand % 8
                jnz -> if (a != 0L) ip = (literalOperand - 2L).toInt()
                bxc -> b = b xor c
                out -> output.add((comboOperand % 8).toString())
                bdv -> b = a shr comboOperand.toInt()
                cdv -> c = a shr comboOperand.toInt()
            }
            ip += 2
        }
    }

    override fun part2(): Long {
        return -1
    }
}
