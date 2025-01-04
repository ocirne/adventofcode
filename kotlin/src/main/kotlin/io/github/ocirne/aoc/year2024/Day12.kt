package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.NSWE

class Day12(val lines: List<String>) : AocChallenge(2024, 12) {

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
                        yield(Position(x + dx, y + dy))
                    }
                }
            }
        }

        operator fun get(p: Position): T {
            return grid[p]!!
        }
    }

    val grid = Grid(lines) { it }

    override fun part1(): Long {
        val plants = grid.grid.values.toSet()
        val areas = grid.grid.map { (_, plant) -> plant }.groupingBy { it }.eachCount()
        val fences = mutableMapOf<Char, Int>()
        grid.grid.map { (position, plant) ->
            val nonNeigbor = 4 - grid.neighbors4S(position).filter { neighbor -> grid[neighbor] == plant }.count()
            fences[plant] = fences.getOrDefault(plant, 0) + nonNeigbor
        }
        println(plants)
        println(areas)
        println(fences)
        return -1
    }

    override fun part2(): Long {
        return -1
    }
}
