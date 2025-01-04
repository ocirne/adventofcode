package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day24(val lines: List<String>) : AocChallenge(2024, 24) {

    private data class Gate(val a: String, val b:String, val c: String, val f: (Int, Int) -> Int)

    private fun readGates(): List<Gate> {
        return lines.dropWhile { it.isNotBlank() }.drop(1).map { line ->
            val (a, op, b, _, c) = line.split(' ')
            when (op) {
                "AND" -> Gate(a, b, c) { x, y -> x and y }
                "OR" -> Gate(a, b, c) { x, y -> x or y }
                "XOR" -> Gate(a, b, c) { x, y -> x xor y }
                else -> throw IllegalArgumentException(op)
            }
        }
    }

    override fun part1(): Long {
        val registers = lines
            .takeWhile { it.isNotBlank() }
            .map { it.split(": ") }
            .associate { (key, value) -> key to value.toInt() }
            .toMutableMap()
        val gates = readGates()
        while (gates.any { it.c !in registers }) {
            gates.forEach { gate ->
                if (gate.c !in registers && gate.a in registers && gate.b in registers) {
                    registers[gate.c] = gate.f(registers[gate.a]!!, registers[gate.b]!!)
                }
            }
        }
        var result = 0L
        for (key in registers.keys.filter { it.startsWith("z") }.sorted().reversed()) {
            result = result shl 1
            result = result or registers[key]!!.toLong()
        }
        return result
    }

    override fun part2(): Long {
        return -1
    }
}
