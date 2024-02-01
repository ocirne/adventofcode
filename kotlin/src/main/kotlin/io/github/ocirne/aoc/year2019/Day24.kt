package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

typealias Bugs = Set<Pair<Int, Int>>

typealias MutableBugs = MutableSet<Pair<Int, Int>>

fun mutableBugs(): MutableBugs = mutableSetOf()

class Day24(val lines: List<String>) : AocChallenge(2019, 24) {

    private fun readBugs(): Bugs {
        val bugs = mutableBugs()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                if (c == '#') {
                    bugs.add(x to y)
                }
            }
        }
        return bugs
    }

    private val NSWE = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    private fun countAdjacentBugs(bugs: Bugs, x: Int, y: Int): Int {
        var total = 0
        for ((dy, dx) in NSWE) {
            if ((x+dx) to (y+dy) in bugs) {
                total += 1
            }
        }
        return total
    }

    private fun nextState(bugs: Bugs): Bugs {
        val nextBugs = mutableBugs()
        IntRange(0, 4).forEach { y ->
            IntRange(0, 4).forEach { x ->
                val adjacent = countAdjacentBugs(bugs, x, y)
                if ((x to y) in bugs && adjacent == 1) {
         //           println("stays: x $x y$y - $adjacent")
                    nextBugs.add(x to y)
                }
                if ((x to y) !in bugs && adjacent in 1..2) {
           //         println("born x $x y $y - $adjacent")
                    nextBugs.add(x to y)
                }
            }
        }
        return nextBugs
    }

    private fun printBugs(bugs: Bugs) {
        println()
        for (y in 0 .. 4) {
            for (x in 0..4) {
                print(if (x to y in bugs) '#' else '.')
            }
            println()
        }
    }

    private fun calculateScore(bugs: Bugs): Int {
        return IntRange(0, 4).sumOf { y ->
            IntRange(0, 4).sumOf { x ->
                if (x to y in bugs) 1 shl y * 5 + x else 0
            }
        }
    }

    override fun part1(): Int {
        var bugs = readBugs()
        val seen = mutableSetOf<Int>()
        while (true) {
          //  printBugs(bugs)
            val score = calculateScore(bugs)
            if (score in seen) {
                println(seen.size)
                return score
            }
            seen.add(score)
            bugs = nextState(bugs)
        }
    }

    override fun part2(): Int {
        return -1
    }
}
