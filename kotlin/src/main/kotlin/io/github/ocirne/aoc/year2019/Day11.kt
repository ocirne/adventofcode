package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day11(val lines: List<String>) : AocChallenge(2019, 11) {

    private class Robot(program: String) {

        val robot = IntCodeEmulator2019(program)
        val panels = mutableMapOf<Pair<Int, Int>, Long>()
        var d = 0
        var x = 0
        var y = 0

        fun paint(startPanel: Long): Robot {
            robot.addInput(startPanel)
            while (!robot.tick()) {
                panels[Pair(x, y)] = robot.getLastOutput()
                robot.tick()
                move(robot.getLastOutput().toInt())
                robot.addInput(panels.getOrDefault(Pair(x, y), 0))
            }
            return this
        }

        private fun move(turn: Int) {
            d = (d + 3 - 2 * turn) % 4
            val (dx, dy) = moves[d]!!
            x += dx
            y += dy
        }

        fun printPanel() {
            val whiteKeys = panels.filter { (_, value) -> value == 1L }.keys
            val y0 = whiteKeys.minOf { (_, y) -> y }
            val x0 = whiteKeys.minOf { (x, _) -> x }
            val y1 = whiteKeys.maxOf { (_, y) -> y }
            val x1 = whiteKeys.maxOf { (x, _) -> x }
            for (y in y0 .. y1) {
                for (x in x0 .. x1) {
                    print(if (panels.getOrDefault(Pair(x, y), 0) == 1L) '#' else ' ')
                }
                println()
            }
        }

        companion object {
            val moves = mapOf(
                0 to Pair(0, -1),
                1 to Pair(+1, 0),
                2 to Pair(0, +1),
                3 to Pair(-1, 0)
            )
        }
    }

    override fun part1(): Int {
        return Robot(lines.first()).paint(0).panels.size
    }

    override fun part2(): String {
        Robot(lines.first()).paint(1).printPanel()
        // read
        return "."
    }
}
