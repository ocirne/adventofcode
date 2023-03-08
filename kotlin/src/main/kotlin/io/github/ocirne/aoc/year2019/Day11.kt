package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day11(val lines: List<String>) : AocChallenge(2019, 11) {

    private fun goForward(d: Int, x: Int, y: Int): Pair<Int, Int> {
        return when (d) {
            0 -> Pair(0, -1)
            1 -> Pair(+1, 0)
            2 -> Pair(0, +1)
            3 -> Pair(-1, 0)
            else -> throw IllegalStateException()
        }
    }

    override fun part1(): Int {
        val robot = IntCodeEmulator2019(lines.first())
        val panels = mutableMapOf<Pair<Int, Int>, Long>()
        robot.addInput(0)
        var d = 0
        var x = 0
        var y = 0
        while (!robot.step()) {
            val color = robot.getLastOutput()
            panels[Pair(x, y)] = color
            robot.step()
            val direction = robot.getLastOutput()
            if (direction == 0L) {
                // turn left
                d = (d + 1) % 4
                val (dx, dy) = goForward(d, x, y)
                x += dx
                y += dy
            } else if (direction == 1L) {
                // turn right
                d = (d + 3) % 4
                val (dx, dy) = goForward(d, x, y)
                x += dx
                y += dy
            } else {
                throw IllegalStateException(direction.toString())
            }
            println("robot output $color $direction :: d $d x $x y $y")
            robot.addInput(panels.getOrDefault(Pair(x, y), 0))
        }
        return panels.size
    }

    override fun part2(): Long {
        TODO()
    }
}


// too high 9746