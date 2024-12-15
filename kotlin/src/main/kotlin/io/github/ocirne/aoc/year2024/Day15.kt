package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

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

    class Grid2(val lines: List<String>) {

        val width = lines.first().length * 2
        val height = lines.size
        var grid = readGrid()
        var oleGrid : Map<Position, Char> = mutableMapOf()
        var robotPosition = findRobot()

        private fun readGrid(): MutableMap<Position, Char> {
            val grid = mutableMapOf<Position, Char>()
            lines.mapIndexed { y, line ->
                line.mapIndexed { x, value ->
                    val (left, right) = when (value) {
                        '#' -> '#' to '#'
                        'O' -> '[' to ']'
                        '.' -> '.' to '.'
                        '@' -> '@' to '.'
                        else -> throw IllegalArgumentException("Unknown value")
                    }
                    grid[Position(2*x, y)] = left
                    grid[Position(2*x + 1, y)] = right
                }
            }
            return grid
        }

        private fun findRobot(): Position {
            return grid.filterValues { it == '@' }.keys.first()
        }

        fun moveRobotX(p: Position, dx: Int): Boolean {
            val currentValue = oleGrid[p]!!
            if (currentValue == '#')
                return false
            if (currentValue == '.')
                return true
            val nextStraight = Position(p.x + dx, p.y)
            val canMove = when (currentValue) {
                '[' -> moveRobotX(nextStraight, dx)
                ']' -> moveRobotX(nextStraight, dx)
                '@' -> moveRobotX(nextStraight, dx)
                else -> throw IllegalArgumentException("Unknown grid element")
            }
            if (canMove) {
                grid[nextStraight] = currentValue
                grid[p] = '.'
            }
            return canMove
        }

        fun tryMoveY(p: Position, dy: Int): Boolean {
            val currentValue = oleGrid[p]!!
            if (currentValue == '#')
                return false
            if (currentValue == '.')
                return true
            val nextStraight = Position(p.x, p.y + dy)
            val nextRight = Position(p.x + 1, p.y + dy)
            val nextLeft = Position(p.x - 1, p.y + dy)
            val canMove = when (currentValue) {
                '@' -> tryMoveY(nextStraight, dy)
                '[' -> tryMoveY(nextStraight, dy) && tryMoveY(nextRight, dy)
                ']' -> tryMoveY(nextStraight, dy) && tryMoveY(nextLeft, dy)
                else -> throw IllegalArgumentException("Unknown grid element")
            }
            val right = Position(p.x + 1, p.y)
            val left = Position(p.x - 1, p.y)
            if (canMove) {
                if (currentValue == '[') {
                    grid[nextRight] = oleGrid[right]!!
                    grid[right] = '.'
                } else if (currentValue == ']') {
                    grid[nextLeft] = oleGrid[left]!!
                    grid[left] = '.'
                }
                grid[nextStraight] = currentValue
                grid[p] = '.'
            }
            return canMove
        }

        fun moveRobot(direction: Char) {
            oleGrid = grid.toMap()
            val moved = when (direction) {
                '^' -> tryMoveY(robotPosition, -1)
                'v' -> tryMoveY(robotPosition, +1)
                '<' -> moveRobotX(robotPosition, -1)
                '>' -> moveRobotX(robotPosition, +1)
                else -> throw IllegalStateException("Unknown: $direction")
            }
            if (moved) {
                robotPosition = findRobot()
            }
        }

        fun print() {
            for (y in 0 until height) {
                for (x in 0 until width) {
                    print(grid[Position(x, y)])
                }
                println()
            }
        }

        fun gps(): Int {
            return grid
                .filterValues { it == '[' }
                .map { (p, _) -> p.x + 100 * p.y }
                .sum()
        }
    }

    override fun part2(): Int {
        val grid = Grid2(lines.takeWhile { it.isNotBlank() })
        for (m in readMovements()) {
            grid.moveRobot(m)
//            grid.print()
        }
        grid.print()
        println("robot: " + grid.robotPosition)
        return grid.gps()
    }
}
