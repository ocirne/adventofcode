package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day13(val lines: List<String>) : AocChallenge(2024, 13) {

    private val buttonA = Regex("Button A: X\\+(\\d+), Y\\+(\\d+)")
    private val buttonB = Regex("Button B: X\\+(\\d+), Y\\+(\\d+)")
    private val prize = Regex("Prize: X=(\\d+), Y=(\\d+)")

    private fun calculateCost(ax: Long, ay: Long, bx: Long, by: Long, px: Long, py: Long): Long {
        val t1 = ay * px - ax * py
        val t2 = ay * bx - ax * by
        if (t1 % t2 != 0L)
            return 0
        val b = t1 / t2
        val t3 = px - b * bx
        if (t3 % ax != 0L)
            return 0
        val a = t3 / ax
        if (a < 0 || b < 0)
            return 0
        return b + 3 * a
    }

    private fun pressButtons(offset: Long = 0L): Long {
        return lines.chunked(4).sumOf { (a, b, p, _) ->
            val (ax, ay) = buttonA.find(a)!!.destructured
            val (bx, by) = buttonB.find(b)!!.destructured
            val (px, py) = prize.find(p)!!.destructured
            calculateCost(
                ax.toLong(), ay.toLong(),
                bx.toLong(), by.toLong(),
                px.toLong() + offset, py.toLong() + offset
            )
        }
    }

    override fun part1(): Long {
        return pressButtons()
    }

    override fun part2(): Long {
        return pressButtons(10000000000000L)
    }
}
