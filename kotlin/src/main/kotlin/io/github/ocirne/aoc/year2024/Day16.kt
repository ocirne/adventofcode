package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.dijkstra

class Day16(val lines: List<String>) : AocChallenge(2024, 16) {

    private data class Position(val x: Int, val y: Int)

    private data class Node(val position: Position, val direction: Char)

    private fun readGrid(): Map<Position, Char> {
        val m = mutableMapOf<Position, Char>()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                if (c != '#') {
                    m[Position(x, y)] = c
                }
            }
        }
        return m.toMap()
    }

    private val moves = mapOf(
        '<' to Position(-1, 0),
        '>' to Position(+1, 0),
        '^' to Position(0, -1),
        'v' to Position(0, +1),
    )

    private val turns = mapOf('<' to "^v", '>' to "^v", '^' to "<>", 'v' to "<>")

    private fun oneSpaceNeighbors(grid: Map<Position, Char>, current: Node): Sequence<Pair<Node, Int>> {
        return sequence {
            val d = moves[current.direction]!!
            val n = Position(current.position.x + d.x, current.position.y + d.y)
            if (grid.contains(n)) {
                yield(Node(n, current.direction) to 1)
            }
            for (nd in turns[current.direction]!!) {
                yield(Node(current.position, nd) to 1000)
            }
        }
    }

    private fun findPosition(grid: Map<Position, Char>, c: Char): Position {
        return grid.filter { (_, value) -> value == c }.keys.first()
    }

    override fun part1(): Int {
        val grid = readGrid()
        val startNode = Node(findPosition(grid, 'S'), '>')
        val endPosition = findPosition(grid, 'E')
        return dijkstra(startNode,
            endCondition = { _, node -> node.position == endPosition },
            neighbors = { position -> oneSpaceNeighbors(grid, position) })
    }

    override fun part2(): Int {
        return -1
    }
}
