package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

typealias Bugs = Set<Pair<Int, Int>>

typealias MutableBugs = MutableSet<Pair<Int, Int>>

typealias PlutoBugs = Set<Triple<Int, Int, Int>>

typealias MutablePlutoBugs = MutableSet<Triple<Int, Int, Int>>

fun mutableBugs(): MutableBugs = mutableSetOf()

fun mutablePlutoBugs(): MutablePlutoBugs = mutableSetOf()

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
            val score = calculateScore(bugs)
            if (score in seen) {
                return score
            }
            seen.add(score)
            bugs = nextState(bugs)
        }
    }

    fun plutonize(bugs: Bugs): PlutoBugs {
        return bugs.map { (x, y) -> Triple(x, y, 0) }.toSet()
    }

    data class Foo(val dx: Int,
                   val dy: Int,
                   val o: (Int, Int) -> Boolean,
                   val i: (Int, Int) -> Boolean,
                   val ob: Pair<Int, Int>) {
        fun isLookAtOuterLevel(x: Int, y: Int): Boolean {
            return o(x, y)
        }

        fun outerLevelBug(z: Int): Triple<Int, Int, Int> {
            val (obx, oby) = ob
            return Triple(obx, oby, z-1)
        }

        fun isLookAtInnerLevel(x: Int, y: Int): Boolean {
            return i(x, y)
        }

        fun innerLevelBugs(z: Int): Sequence<Triple<Int, Int, Int>> {
            return sequence {
                if (dx == -1) {  // left
                    for (i in 0..4) {
                        yield(Triple(4, i, z + 1))
                    }
                }
                if (dx == 1) {  // right
                    for (i in 0..4) {
                        yield(Triple(0, i, z + 1))
                    }
                }
                if (dy == -1) {  // up
                    for (i in 0..4) {
                        yield(Triple(i, 4, z + 1))
                    }
                }
                if (dy == 1) {  // down
                    for (i in 0..4) {
                        yield(Triple(i, 0, z + 1))
                    }
                }
            }
        }
    }

    private val NSWE_PLUTO = listOf(
        // up
        Foo(0, -1, {x, y -> y == 0}, {x, y -> x == 2 && y == 3}, 2 to 1),
        // down
        Foo(0, 1, {x, y -> y == 4}, {x, y -> x == 2 && y == 1}, 2 to 3),
        // left
        Foo(-1, 0, {x, y -> x == 0}, {x, y -> x == 3 && y == 2}, 1 to 2),
        // right
        Foo(1, 0, {x, y -> x == 4}, {x, y -> x == 1 && y == 2}, 3 to 2),
    )

    private fun countAdjacentBugsPluto(bugs: PlutoBugs, x: Int, y: Int, z: Int): Int {
        var total = 0
        for (a in NSWE_PLUTO) {
            if (a.isLookAtOuterLevel(x, y)) {
                if (a.outerLevelBug(z) in bugs) {
                    total += 1
                }
            } else if (a.isLookAtInnerLevel(x, y)) {
                for (b in a.innerLevelBugs(z)) {
                    if (b in bugs) {
                        total += 1
                    }
                }
            } else { // same level
                if (Triple(x+a.dx, y+a.dy, z) in bugs) {
                    total += 1
                }
            }
        }
        return total
    }

    private fun nextStatePluto(bugs: PlutoBugs, i: Int): PlutoBugs {
        val nextBugs = mutablePlutoBugs()
        IntRange(0, 4).forEach { x ->
            IntRange(0, 4).forEach { y ->
                IntRange(-i, i).forEach { z ->
                    if (!(x == 2 && y == 2)) {
                        val adjacent = countAdjacentBugsPluto(bugs, x, y, z)
                        val t = Triple(x, y, z)
                        if (t in bugs && adjacent == 1) {
                            nextBugs.add(t)
                        }
                        if (t !in bugs && adjacent in 1..2) {
                            nextBugs.add(t)
                        }
                    }
                }
            }
        }
        return nextBugs
    }

    private fun printPlutoBugs(bugs: PlutoBugs) {
        println()
        for (z in -7 .. 7) {
            println("z = $z:")
            for (y in 0..4) {
                for (x in 0..4) {
                    print(if (Triple(x, y, z) in bugs) '#' else '.')
                }
                println()
            }
            println()
        }
    }

    private fun countBugs(bugs: PlutoBugs): Int {
        return bugs.size
    }

    fun simulate(minutes: Int): Int {
        var bugs = plutonize(readBugs())
        repeat(minutes) {
            bugs = nextStatePluto(bugs, it+1)
        }
        printPlutoBugs(bugs)
        return countBugs(bugs)
    }

    override fun part2(): Int {
        return simulate(200)
    }
}
