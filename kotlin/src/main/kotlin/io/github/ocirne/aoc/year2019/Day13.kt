package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.year2019.IntCodeEmulator2019.Companion.ReturnCode.*

class Day13(val lines: List<String>) : AocChallenge(2019, 13) {

    private class Arcade(program: String) {

        val arcade = IntCodeEmulator2019(program)
        val screen = mutableMapOf<Pair<Long, Long>, Long>()

        var paddleX = 0L
        var ballX = 0L

        var score = 0L

        fun paint(): Arcade {
            while (true) {
                val (x, y, tileId) = arcade.getNextOutputs(3) ?: return this
                screen[x to y] = tileId
            }
        }

        fun loopOutput(): Sequence<Long> {
            return sequence {
                while (true) {
                    when (arcade.tick2()) {
                        NEED_INPUT -> arcade.addInput(ballX.compareTo(paddleX).toLong())
                        HAS_OUTPUT -> yield(arcade.getLastOutput())
                        STOP -> break
                    }
                }
            }
        }

        fun playGame(): Long {
            for ((x, y, tileId) in loopOutput().chunked(3)) {
                when {
                    (x == -1L && y == 0L) -> score = tileId
                    tileId == 3L -> paddleX = x
                    tileId == 4L -> ballX = x
                }
            }
            return score
        }
    }

    override fun part1(): Int {
        return Arcade(lines.first()).paint().screen.values.filter { it == 2L }.size
    }

    override fun part2(): Long {
        val arcade = Arcade(lines.first())
        arcade.arcade.program[0L] = 2L
        return arcade.playGame()
    }
}
