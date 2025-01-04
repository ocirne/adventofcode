package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day7(val lines: List<String>) : AocChallenge(2024, 7) {

    private fun check(value: Long, numbers: List<Long>): Boolean {
        if (numbers.size == 1) {
            return value == numbers.first()
        }
        val (first, second) = numbers.take(2)
        val rest = numbers.drop(2)
        return check(value, listOf(first + second) + rest) || check(value, listOf(first * second) + rest)
    }

    override fun part1(): Long {
        var total = 0L
        for (line in lines) {
            val (value, rest) = line.split(": ")
            val numbers = rest.split(' ').map { it.toLong() }
            if (check(value.toLong(), numbers)) {
                total += value.toLong()
            }
        }
        return total
    }

    private fun check2(value: Long, numbers: List<Long>): Boolean {
        if (numbers.size == 1) {
            return value == numbers.first()
        }
        val (first, second) = numbers.take(2)
        val rest = numbers.drop(2)
        return check2(value, listOf(first + second) + rest) ||
                check2(value, listOf(first * second) + rest) ||
                check2(value, listOf((first.toString() + second.toString()).toLong()) + rest)
    }

    override fun part2(): Long {
        var total = 0L
        for (line in lines) {
            val (value, rest) = line.split(": ")
            val numbers = rest.split(' ').map { it.toLong() }
            if (check2(value.toLong(), numbers)) {
                total += value.toLong()
            }
        }
        return total
    }
}
