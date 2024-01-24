package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.util.*

val nswe = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

class Day20(val lines: List<String>) : AocChallenge(2019, 20) {

    data class Position(val x: Int, val y: Int)

    data class Portal(val label: String, val position: Position, val circle: Int)

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

    private fun isOuterPortal(x: Int, y: Int, width: Int, height: Int): Boolean {
        return x == 2 || y == 2 || x == width - 3 || y == height - 3
    }

    private fun findPortals(): List<Portal> {
        val width = lines.maxOf { it.length }
        val height = lines.size
        println("w h $width $height")
        for (y in height - 5 .. height-3) {
            for (x in width - 5..width - 3) {
                print(lines[y][x])
            }
            println()
        }
        val m = mutableListOf<Portal>()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                isPortal(y, x, c)?.let {label ->
                    if (isOuterPortal(x, y, width, height)) {
                        m.add(Portal(label, Position(x, y), -1))
                    } else {
                        m.add(Portal(label, Position(x, y), +1))
                    }
                }
            }
        }
        return m.toList()
    }

    class LabNode(val steps: Int, val position: Position): Comparable<LabNode> {

        fun neighbors(lines: List<String>): Sequence<LabNode> {
            val (x, y) = position
            return sequence {
                for ((dy, dx) in nswe) {
                    if (lines[y+dy][x+dx] == '.') {
                        yield(LabNode(steps + 1, Position(x + dx, y + dy)))
                    }
                }
            }
        }

        override fun compareTo(other: LabNode): Int {
            return steps.compareTo(other.steps)
        }
    }

    private fun exploreMap2(portals: List<Portal>, anders: Map<Position, Portal>, startPortal: Portal): Map<Portal, Int> {
        val openHeap = PriorityQueue<LabNode>()
        val visited = mutableMapOf<Position, LabNode>()
        openHeap.add(LabNode(0, startPortal.position))
        val neighbors = mutableMapOf<Portal, Int>()
        while (openHeap.isNotEmpty()) {
            val node = openHeap.remove()
            if (node.position in anders && node.steps > 0) {
                println("  ${anders[node.position]} in ${node.steps}")
                neighbors.put(anders[node.position]!!, node.steps)
            }
            visited[node.position] = node
            for (neighbor in node.neighbors(lines)) {
                if (visited.contains(neighbor.position)) {
                    continue
                }
                openHeap.add(neighbor)
            }
        }
        assert(!neighbors.contains(startPortal))
        if (startPortal.label != "AA" && startPortal.label != "ZZ") {
            val otherPortal = portals.single { it.label == startPortal.label && it.circle != startPortal.circle }
            neighbors[otherPortal] = 1
        }
        return neighbors
    }

    private fun compactifyGraph(portals: List<Portal>): Map<Portal, Map<Portal, Int>> {
        val anders = portals.associateBy { portal -> portal.position }
        return portals.associateWith { portal -> exploreMap2(portals, anders, portal) }
    }

    class Node(val g: Int, val portal: Portal): Comparable<Node> {

        override fun compareTo(other: Node): Int {
            return g.compareTo(other.g)
        }
    }

    private fun exploreMap(graph: Map<Portal, Map<Portal, Int>>, startPortal: Portal, endPortal: Portal): Int {
        val openHeap = PriorityQueue<Node>()
        val closedSet = mutableSetOf<Portal>()
        val g = mutableMapOf(startPortal to 0, endPortal to Int.MAX_VALUE)
        openHeap.add(Node(0, startPortal))
        while (openHeap.isNotEmpty()) {
            val current = openHeap.remove()
            if (current.g > g[endPortal]!!) {
                break
            }
            val currentPortal = current.portal
            if (currentPortal == endPortal) {
                println("g ${currentPortal} ${g[currentPortal]}")
            }
            closedSet.add(currentPortal)
            println("expand $currentPortal")
            for ((neighborPortal, distance) in graph[currentPortal]!!) {
                val tg = g[currentPortal]!! + distance
                println("neighbor ${neighborPortal}, ${tg}")
                if (neighborPortal in closedSet && tg >= g[neighborPortal]!!) {
                    continue
                }
                if (tg < g.getOrDefault(neighborPortal, 0) || ! openHeap.map { it.portal }.contains(neighborPortal)) {
                    g[neighborPortal] = tg
                    openHeap.add(Node(tg, neighborPortal))
                }
            }
        }
        return g[endPortal]!!
    }

    override fun part1(): Int {
        val portals = findPortals()
        println(portals)
        val graph = compactifyGraph(portals)
        println(graph)
        val startPortal = portals.single { it.label == "AA" }
        val endPortal = portals.single { it.label == "ZZ" }
        return exploreMap(graph, startPortal, endPortal)
    }

    override fun part2(): Int {
        val portals = findPortals()
        println(portals)
        val graph = compactifyGraph(portals)
        println("compact graph: $graph")
//        return exploreMap(graph)
        return -1
    }
}
