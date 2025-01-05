package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.NSWE

class Day10(val lines: List<String>) : AocChallenge(2024, 10) {

    data class Position(val x: Int, val y: Int)

    class Grid<T>(val lines: List<String>, val interpretValue: (Char) -> T) {

        val width = lines.firstOrNull()?.length
        val height = lines.size
        val grid = readGrid()

        private fun readGrid(): Map<Position, T> {
            val grid = mutableMapOf<Position, T>()
            lines.mapIndexed { y, line ->
                line.mapIndexed { x, value ->
                    grid[Position(x, y)] = interpretValue(value)
                }
            }
            return grid
        }

        fun neighbors4S(p: Position): Sequence<Position> {
            val (x, y) = p
            return sequence {
                for ((dx, dy) in NSWE) {
                    if (x + dx in 0 until width!! && y + dy in 0 until height) {
                        yield(Position (x + dx, y+dy))
                    }
                }
            }
        }

        operator fun get(p: Position): T {
            return grid[p]!!
        }
    }

    private fun search(grid: Grid<Int>, position: Position): Long {
        val value = grid[position]
        if (value == 9) {
            foo.putIfAbsent(position, 0)
            foo[position] = foo[position]!! + 1
            return 1
        }
        var total = 0L
        for (neighbor in grid.neighbors4S(position)) {
            if (grid[neighbor] != value + 1) {
                continue
            }
            total += search(grid, neighbor)
        }
        return total
    }

    private val grid = Grid(lines) { value -> value.digitToInt() }

    // TODO
    private var foo = mutableMapOf<Position, Int>()

    override fun part1(): Long {
        var total = 0L
        grid.grid.map { start ->
            if (start.value == 0) {
                foo.clear()
                search(grid, start.key)
                total += foo.size
                println(foo.size)
            }
        }
        return total
    }

    override fun part2(): Long {
        var total = 0L
        grid.grid.map { start ->
            if (start.value == 0) {
                foo.clear()
                search(grid, start.key)
                total += foo.map { it.value }.sum()
                println(foo.size)
            }
        }
        return total
    }
}
