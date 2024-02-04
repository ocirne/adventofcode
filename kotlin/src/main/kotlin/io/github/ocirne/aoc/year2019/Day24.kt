package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.NSWE

data class Bug(val x: Int, val y: Int, val z: Int)

typealias Bugs = Set<Bug>

typealias MutableBugs = MutableSet<Bug>

fun mutableBugs(): MutableBugs = mutableSetOf()

class Day24(val lines: List<String>) : AocChallenge(2019, 24) {

    private abstract class BugLife(lines: List<String>) {

        var bugs = readBugs(lines)

        fun nextState(i: Int, ignoreMiddle: Boolean = false) {
            val nextBugs = mutableBugs()
            IntRange(0, 4).forEach { x ->
                IntRange(0, 4).forEach { y ->
                    IntRange(-i, i).forEach { z ->
                        if (!(ignoreMiddle && x == 2 && y == 2)) {
                            val b = Bug(x, y, z)
                            val adjacent = countAdjacentBugs(b)
                            if (b in bugs && adjacent == 1) {
                                nextBugs.add(b)
                            }
                            if (b !in bugs && adjacent in 1..2) {
                                nextBugs.add(b)
                            }
                        }
                    }
                }
            }
            bugs = nextBugs
        }

        abstract fun countAdjacentBugs(b: Bug): Int

        companion object {
            private fun readBugs(lines: List<String>): Bugs {
                val bugs = mutableBugs()
                lines.forEachIndexed { y, line ->
                    line.forEachIndexed { x, c ->
                        if (c == '#') {
                            bugs.add(Bug(x, y, 0))
                        }
                    }
                }
                return bugs
            }
        }
    }

    private class SimpleBugLife(lines: List<String>): BugLife(lines) {

        override fun countAdjacentBugs(b: Bug): Int {
            return NSWE.filter { (dx, dy) -> bugs.contains(Bug(b.x+dx, b.y+dy, 0)) }.size
        }

        fun calculateScore(): Int {
            return IntRange(0, 4).sumOf { y ->
                IntRange(0, 4).sumOf { x ->
                    if (Bug(x, y, 0) in bugs) 1 shl y * 5 + x else 0
                }
            }
        }
    }

    private class PlutoBugLive(lines: List<String>): BugLife(lines) {

        data class NeighborDescription(val dx: Int,
                                       val dy: Int) {

            fun isLookAtOuterLevel(x: Int, y: Int): Boolean {
                return if (dx != 0) x == 2*dx + 2 else y == 2*dy + 2
            }

            fun outerLevelBug(z: Int): Bug {
                val ox = if (dx != 0) 2 + dx else 2
                val oy = if (dy != 0) 2 + dy else 2
                return Bug(ox, oy, z-1)
            }

            fun isLookAtInnerLevel(x: Int, y: Int): Boolean {
                val ox = if (dx != 0) 2 - dx else 2
                val oy = if (dy != 0) 2 - dy else 2
                return x == ox && y == oy
            }

            fun innerLevelBugs(z: Int): Sequence<Bug> {
                return sequence {
                    for (i in 0..4) {
                        val ix = if (dx != 0) -2*dx + 2 else i
                        val iy = if (dy != 0) -2*dy + 2 else i
                        yield(Bug(ix, iy, z + 1))
                    }
                }
            }
        }

        private val NSWE_PLUTO = listOf(
            NeighborDescription(0, -1),
            NeighborDescription(0, 1),
            NeighborDescription(-1, 0),
            NeighborDescription(1, 0),
        )

        override fun countAdjacentBugs(b: Bug): Int {
            return NSWE_PLUTO.map { a ->
                if (a.isLookAtOuterLevel(b.x, b.y)) {
                    if (a.outerLevelBug(b.z) in bugs) 1 else 0
                } else if (a.isLookAtInnerLevel(b.x, b.y)) {
                    a.innerLevelBugs(b.z).filter { it in bugs }.count()
                } else { // same level
                    if (Bug(b.x+a.dx, b.y+a.dy, b.z) in bugs) 1 else 0
                }
            }.sum()
        }
    }

    override fun part1(): Int {
        val bugs = SimpleBugLife(lines)
        val seen = mutableSetOf<Int>()
        while (true) {
            val score = bugs.calculateScore()
            if (score in seen) {
                return score
            }
            seen.add(score)
            bugs.nextState(0)
        }
    }

    fun simulate(minutes: Int): Int {
        val bugs = PlutoBugLive(lines)
        repeat(minutes) {
            bugs.nextState(it+1, ignoreMiddle = true)
        }
        return bugs.bugs.size
    }

    override fun part2(): Int {
        return simulate(200)
    }
}
