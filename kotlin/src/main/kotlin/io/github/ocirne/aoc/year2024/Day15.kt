package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day15(val lines: List<String>) : AocChallenge(2024, 15) {

    private data class Position(val x: Int, val y: Int)

    private class WarehouseGrid(val lines: List<String>, val twiceAsWide: Boolean) {

        val width = lines.first().length * (if (twiceAsWide) 2 else 1)
        val height = lines.size
        var grid = readGrid()
        var robotPosition = findRobot()

        private fun readGrid(): MutableMap<Position, Char> {
            val grid = mutableMapOf<Position, Char>()
            lines.mapIndexed { y, line ->
                line.mapIndexed { x, value ->
                    if (!twiceAsWide) {
                        grid[Position(x, y)] = value
                    } else {
                        val (left, right) = when (value) {
                            '#' -> '#' to '#'
                            'O' -> '[' to ']'
                            '.' -> '.' to '.'
                            '@' -> '@' to '.'
                            else -> throw IllegalArgumentException("Unknown value")
                        }
                        grid[Position(2 * x, y)] = left
                        grid[Position(2 * x + 1, y)] = right
                    }
                }
            }
            return grid
        }

        private fun findRobot(): Position {
            return grid.filterValues { it == '@' }.keys.first()
        }

        private fun checkNextLayer(dx: Int, dy: Int, layer: Set<Position>): Boolean {
            if (layer.any { p -> grid[p] == '#'})
                throw IllegalStateException("shouldn't be #")
            if (layer.all { p -> grid[p] == '.'}) {
                return true
            }
            val nextLayer: MutableSet<Position> = mutableSetOf()
            for (p in layer) {
                val nextStraight = Position(p.x + dx, p.y + dy)
                when (grid[nextStraight]!!) {
                    'O' -> {
                        nextLayer.add(nextStraight)
                    }
                    ']' -> {
                        nextLayer.add(nextStraight)
                        if (dx == 0)
                            // west
                            nextLayer.add(Position(p.x - 1, p.y + dy))
                    }
                    '[' -> {
                        nextLayer.add(nextStraight)
                        if (dx == 0)
                            // east
                            nextLayer.add(Position(p.x + 1, p.y + dy))
                    }
                    '.' -> {}
                    '#' -> return false
                    else -> throw IllegalArgumentException("Unknown grid element")
                }
            }
            val movedNextLayer = checkNextLayer(dx, dy, nextLayer)
            if (movedNextLayer) {
                for (p in layer) {
                    val nextPosition = Position(p.x + dx, p.y + dy)
                    grid[nextPosition] = grid[p]!!
                    grid[p] = '.'
                }
            }
            return movedNextLayer
        }

        fun moveRobot(direction: Char) {
            val moved = when (direction) {
                '^' -> checkNextLayer(0, -1, setOf(robotPosition))
                'v' -> checkNextLayer(0, +1, setOf(robotPosition))
                '<' -> checkNextLayer(-1, 0, setOf(robotPosition))
                '>' -> checkNextLayer(+1, 0, setOf(robotPosition))
                else -> throw IllegalStateException("Unknown: $direction")
            }
            if (moved) {
                robotPosition = findRobot()
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
                .filterValues { it == 'O' || it == '[' }
                .map { (p, _) -> p.x + 100 * p.y }
                .sum()
        }
    }

    private fun readMovements(): String {
        return lines.dropWhile { it.isNotBlank() }.drop(1).joinToString("")
    }

    private fun searchWarehouse(twiceAsWide: Boolean): Int {
        val grid = WarehouseGrid(lines.takeWhile { it.isNotBlank() }, twiceAsWide)
        for (m in readMovements()) {
            grid.moveRobot(m)
        }
        return grid.gps()

    }

    override fun part1(): Int {
        return searchWarehouse(false)
    }

    override fun part2(): Int {
        return searchWarehouse(true)
    }
}
