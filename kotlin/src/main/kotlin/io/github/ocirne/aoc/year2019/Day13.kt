package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day13(val lines: List<String>) : AocChallenge(2019, 13) {

    private class Arcade(program: String) {

        val arcade = IntCodeEmulator2019(program)
        val screen = mutableMapOf<Pair<Long, Long>, Long>()

        fun paint(): Arcade {
            while (true) {
                val (x, y, tileId) = arcade.getNextOutputs(3) ?: return this
                screen[x to y] = tileId
            }
        }

        companion object {
            val TILES = mapOf(
                0 to "empty tile",
                1 to "wall",
                2 to "block",
                3 to "horizontal paddle",
                4 to "ball"
            )
        }
    }

    override fun part1(): Int {
        return Arcade(lines.first()).paint().screen.values.filter { it == 2L }.size
    }

    override fun part2(): String {
        return "."
    }
}
