package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.util.*

val nswe = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

class Day20(val lines: List<String>) : AocChallenge(2019, 20) {

    data class Position(val x: Int, val y: Int)

    private fun isPortal(y: Int, x: Int, c: Char): String? {
        if (c != '.') {
            return null
        }
        for ((dy, dx) in nswe) {
            val c1 = lines[y+dy][x+dx]
            if (c1.isLetter()) {
                val c2 = lines[y+dy+dy][x+dx+dx]
                assert(c2.isLetter())
                return if (c1 < c2) "$c1$c2" else "$c2$c1"
            }
        }
        return null
    }

    private fun findPortals(): Map<Position, String> {
        val m = mutableMapOf<Position, String>()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                isPortal(y, x, c)?.let {label ->
                    m[Position(x, y)] = label
                }
            }
        }
        return m.toMap()
    }

    class Node(val portals: Map<Position, String>, val steps: Int, val position: Position): Comparable<Node> {

        fun isEnd(): Boolean {
            return portals[position] == "ZZ"
        }

        fun neighbors(lines: List<String>): Sequence<Node> {
            val (x, y) = position
            return sequence {
                for ((dy, dx) in nswe) {
                    if (lines[y+dy][x+dx] == '.') {
                        yield(Node(portals, steps + 1, Position(x + dx, y + dy)))
                    }
                }
                if (position in portals) {
                    val label = portals[position]
                    if (label != "AA") {
                        val otherPortal =
                            portals.filter { (otherPosition, otherLabel) -> position != otherPosition && otherLabel == label }.keys.single()
                        yield(Node(portals, steps + 1, otherPortal))
                    }
                }
            }
        }

        override fun compareTo(other: Node): Int {
            return steps.compareTo(other.steps)
        }
    }

    private fun exploreMap(portals: Map<Position, String>, startNode: Node): Int {
        val openHeap = PriorityQueue<Node>()
        val visited = mutableMapOf<Position, Node>()
        openHeap.add(Node(portals, 0, startNode.position))
        while (openHeap.isNotEmpty()) {
            val node = openHeap.remove()
            if (node.isEnd()) {
                return node.steps
            }
            visited[node.position] = node
            for (neighbor in node.neighbors(lines)) {
                if (visited.contains(neighbor.position)) {
                    continue
                }
                openHeap.add(neighbor)
            }
        }
        throw IllegalStateException()
    }

    override fun part1(): Int {
        val portals = findPortals()
        val startPosition = portals.filter { (_, label) -> label == "AA" }.keys.single()
        val startNode = Node(portals, 0, startPosition)
        return exploreMap(portals, startNode)
    }

    override fun part2(): Int {
        return -1
    }
}
