package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.ComparableNode
import io.github.ocirne.aoc.NSWE
import java.util.*
import kotlin.math.abs

class Day20(val lines: List<String>) : AocChallenge(2024, 20) {

    private data class Position(val x: Int, val y: Int)

    private fun readGrid(): Map<Position, Char> {
        val m = mutableMapOf<Position, Char>()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                m[Position(x, y)] = c
            }
        }
        return m.toMap()
    }

    private fun directNeighbors(grid: Map<Position, Char>, current: Position): Sequence<Position> {
        return sequence {
            for ((dx, dy) in NSWE) {
                val n = Position(current.x + dx, current.y + dy)
                if (grid.getOrDefault(n, '#') != '#') {
                    yield(n)
                }
            }
        }
    }

    private fun findPosition(grid: Map<Position, Char>, c: Char): Position {
        return grid.filter { (_, value) -> value == c }.keys.first()
    }

    // Returns: A Grid, where every path is has the cost to the end.
    private fun flodder(startNode: Position,
                        neighbors: (Position) -> Sequence<Position>): Map<Position, Int> {
        val openHeap = PriorityQueue<ComparableNode<Position>>()
        val closedSet = mutableSetOf<Position>()
        val g = mutableMapOf(startNode to 0)
        openHeap.add(ComparableNode(0, startNode))
        while (openHeap.isNotEmpty()) {
            val current = openHeap.remove()
            closedSet.add(current.node)
            for (neighborNode in neighbors(current.node)) {
                val tg = g[current.node]!! + 1
                if (neighborNode in closedSet && tg >= g[neighborNode]!!) {
                    continue
                }
                if (tg <= g.getOrDefault(neighborNode, 0) || ! openHeap.map { it.node }.contains(neighborNode)) {
                    g[neighborNode] = tg
                    openHeap.add(ComparableNode(tg, neighborNode))
                }
            }
        }
        return g
    }

    private fun listCheats2(g: Map<Position, Int>): List<Int> {
        val result = mutableListOf<Int>()
        for ((p0, cost) in g) {
            for ((dx, dy) in NSWE) {
                val p1 = Position(p0.x + dx, p0.y + dy)
                val p2 = Position(p0.x + 2 * dx, p0.y + 2 * dy)
                if (!g.contains(p1)
                    && g.contains(p2)) {
                    val diff = cost - g[p2]!! - 2
                    if (diff > 0) {
                        result.add(diff)
                    }
                }
            }
        }
        return result.toList()
    }

    override fun part1(): Int {
        val grid = readGrid()
        val startNode = findPosition(grid, 'E')
        val g = flodder(startNode,
            neighbors = { position -> directNeighbors(grid, position) })
        var total = 0
        for ((saved, count) in listCheats2(g).groupingBy { it }.eachCount()) {
            if (saved >= 100) {
                total += count
            }
        }
        return total
    }

    private fun listCheats20(g: Map<Position, Int>): List<Int> {
        val result = mutableListOf<Int>()
        val N = 20
        for ((p0, cost) in g) {
            for (dx in -N .. N) {
                for (dy in -N .. N) {
                    val cheatLength = abs(dx) + abs(dy)
                    if (cheatLength > N) {
                        continue
                    }
                    // ignore cheats length 2
                    if (cheatLength < 3) {
                        continue
                    }
                    // assumption: every cheat > 3 exists
                    val p2 = Position(p0.x + dx, p0.y + dy)
                    if (g.contains(p2)) {
                        val diff = cost - g[p2]!! - cheatLength
                        if (diff > 0) {
                            result.add(diff)
                        }
                    }
                }
            }
        }
        return result.toList()
    }

    override fun part2(): Int {
        val grid = readGrid()
        val startNode = findPosition(grid, 'E')
        val g = flodder(startNode,
            neighbors = { position -> directNeighbors(grid, position) })
        var total = 0
        for ((saved, count) in listCheats20(g).groupingBy { it }.eachCount()) {
            if (saved >= 100) {
                total += count
            }
        }
        val count2 = part1()
        return count2 + total
    }
}
