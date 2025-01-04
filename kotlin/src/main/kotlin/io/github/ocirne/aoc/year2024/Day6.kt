package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day6(val lines: List<String>) : AocChallenge(2024, 6) {

    override fun part1(): Int {
        val width = lines.first().length
        val height = lines.size
        val obstacles = mutableSetOf<Pair<Int, Int>>()
        var px = 0
        var py = 0
        var direction = '^'
        lines.mapIndexed { y, line ->
            line.mapIndexed { x, value ->
                if (value == '#') {
                    obstacles.add(x to y)
                }
                if (value == '^') {
                    px = x
                    py = y
                }
            }
        }
        val visited = mutableSetOf<Pair<Int, Int>>()
        while (true) {
            visited.add(px to py)
            val (dx, dy) = when (direction) {
                '^' -> (0 to -1)
                'v' -> (0 to 1)
                '<' -> (-1 to 0)
                '>' -> (1 to 0)
                else -> throw NotImplementedError()
            }
            val nx = px + dx
            val ny = py + dy
            if (nx < 0 || nx >= width || ny < 0 || ny >= height) {
                return visited.size
            }
            if (obstacles.contains(nx to ny)) {
                direction = when (direction) {
                    '^' -> '>'
                    'v' -> '<'
                    '<' -> '^'
                    '>' -> 'v'
                    else -> throw NotImplementedError()
                }
            } else {
                px = nx
                py = ny
            }
        }
    }

    private fun hasLoop(width: Int, height: Int, obstacles: Set<Pair<Int, Int>>, sx: Int, sy: Int): Boolean {
        var px = sx
        var py = sy
        var direction = '^'
        val visited = mutableSetOf<Triple<Int, Int, Char>>()
        while (true) {
            if (visited.contains(Triple(px, py, direction))) {
                return true
            }
            visited.add(Triple(px, py, direction))
            val (dx, dy) = when (direction) {
                '^' -> (0 to -1)
                'v' -> (0 to 1)
                '<' -> (-1 to 0)
                '>' -> (1 to 0)
                else -> throw NotImplementedError()
            }
            val nx = px + dx
            val ny = py + dy
            if (nx < 0 || nx >= width || ny < 0 || ny >= height) {
                return false
            }
            if (obstacles.contains(nx to ny)) {
                direction = when (direction) {
                    '^' -> '>'
                    'v' -> '<'
                    '<' -> '^'
                    '>' -> 'v'
                    else -> throw NotImplementedError()
                }
            } else {
                px = nx
                py = ny
            }
        }
    }

    override fun part2(): Int {
        val width = lines.first().length
        val height = lines.size
        val obstacles = mutableSetOf<Pair<Int, Int>>()
        var px = 0
        var py = 0
        lines.mapIndexed { y, line ->
            line.mapIndexed { x, value ->
                if (value == '#') {
                    obstacles.add(x to y)
                }
                if (value == '^') {
                    px = x
                    py = y
                }
            }
        }
        var total = 0
        for (oy in 0 until height) {
            for (ox in 0 until height) {
                if (obstacles.contains(ox to oy)) {
                    continue
                }
                obstacles.add(ox to oy)
                if (hasLoop(width, height, obstacles, px, py)) {
                    total++
                }
                obstacles.remove(ox to oy)
            }
        }
        return total
    }
}
