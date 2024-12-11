package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day11(val lines: List<String>) : AocChallenge(2024, 11) {

    fun step(n: List<Long>): List<Long> {
        val r = mutableListOf<Long>()
        for (x in n) {
//            println("#" + x + "<")
            val s = x.toString()
            when {
                x == 0L -> r.add(1)
                s.length % 2 == 0 -> {
                    r.add(s.substring(0, s.length / 2).toLong())
                    r.add(s.substring(s.length / 2, s.length).toLong())
                }
                else -> r.add(2024 * x)
            }
        }
        return r
    }

    override fun part1(): Int {
        var numbers = lines.first().trim().split(' ').map { it.toLong() }
        repeat(25) {
            numbers = step(numbers)
        }
        return numbers.size
    }

    val seen = mutableMapOf<Pair<Long, Int>, Long>()

    fun step2(x: Long, step: Int): Long {
        if (x to step in seen) {
            return seen[x to step]!!
        }
        if (step == 0)
            return 1
        val s = x.toString()
        val r = when {
            x == 0L -> step2(1, step - 1)
            s.length % 2 == 0 -> {
                step2(s.substring(0, s.length / 2).toLong(), step - 1) + step2(s.substring(s.length / 2, s.length).toLong(), step - 1)
            }
            else -> step2(2024 * x, step - 1)
            }
        seen[x to step] = r
        return r
    }

    override fun part2(): Long {
        var numbers = lines.first().trim().split(' ').map { it.toLong() }
        var total = 0L
        for (n in numbers) {
            total += step2(n, 75)
        }
        return total
    }
}
