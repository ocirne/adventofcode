package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.NSWE

class Day15(val lines: List<String>) : AocChallenge(2024, 15) {

    data class Position(val x: Int, val y: Int)

    class Grid(val lines: List<String>) {

        val width = lines.firstOrNull()?.length
        val height = lines.size
        val grid = readGrid()
        var robot = findRobot()

        private fun readGrid(): MutableMap<Position, Char> {
            val grid = mutableMapOf<Position, Char>()
            lines.mapIndexed { y, line ->
                line.mapIndexed { x, value ->
                    grid[Position(x, y)] = value
                }
            }
            return grid
        }

        private fun findRobot(): Position {
            return grid.filterValues { it == '@' }.keys.first()
        }

        fun moveRobot(p: Position, dx: Int, dy: Int): Boolean {
            val nextPosition = Position(p.x + dx, p.y + dy)
            val canMove = when (grid[nextPosition]!!) {
                'O' -> moveRobot(nextPosition, dx, dy)
                '#' -> false
                '.' -> true
                '@' -> throw IllegalArgumentException("found another robot")
                else -> throw IllegalArgumentException("Unknown grid element")
            }
            if (canMove) {
                grid[nextPosition] = grid[p]!!
                grid[p] = '.'
            }
            return canMove
        }

        fun moveRobot(direction: Char) {
            val moved = when (direction) {
                '^' -> moveRobot(robot, 0, -1)
                'v' -> moveRobot(robot, 0, +1)
                '<' -> moveRobot(robot, -1, 0)
                '>' -> moveRobot(robot, +1, 0)
                else -> throw IllegalStateException("Unknown: $direction")
            }
            if (moved) {
                robot = findRobot()
            }
        }

        operator fun get(p: Position): Char {
            return grid[p]!!
        }

        fun print() {
            for (y in 0 until height) {
                for (x in 0 until width!!) {
                    print(grid[Position(x, y)])
                }
                println()
            }
        }

        fun gps(): Int {
            return grid
                .filterValues { it == 'O' }
                .map { (p, _) -> p.x + 100 * p.y }
                .sum()
        }
    }

    private fun readMovements(): String {
        return lines.dropWhile { it.isNotBlank() }.drop(1).joinToString("")
    }

    override fun part1(): Int {
        val grid = Grid(lines.takeWhile { it.isNotBlank() })
        for (m in readMovements()) {
            grid.moveRobot(m)
        }
        grid.print()
        println("robot: " + grid.robot)
        return grid.gps()
    }

    override fun part2(): Int {
        return -1
    }
}
