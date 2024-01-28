package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.util.*

private class ComparableNode<N>(val g: Int, val node: N): Comparable<ComparableNode<N>> {

    override fun compareTo(other: ComparableNode<N>): Int {
        return g.compareTo(other.g)
    }
}

private fun <N> dijkstra(startNode: N, endNode: N, neighbors: (N) -> Map<N, Int>): Int {
    val openHeap = PriorityQueue<ComparableNode<N>>()
    val closedSet = mutableSetOf<N>()
    val g = mutableMapOf(startNode to 0, endNode to Int.MAX_VALUE)
    openHeap.add(ComparableNode(0, startNode))
    while (openHeap.isNotEmpty()) {
        val current = openHeap.remove()
        if (current.g > g[endNode]!!) {
            break
        }
        closedSet.add(current.node)
        for ((neighborNode, distance) in neighbors(current.node)) {
            val tg = g[current.node]!! + distance
            if (neighborNode in closedSet && tg >= g[neighborNode]!!) {
                continue
            }
            if (tg < g.getOrDefault(neighborNode, 0) || ! openHeap.map { it.node }.contains(neighborNode)) {
                g[neighborNode] = tg
                openHeap.add(ComparableNode(tg, neighborNode))
            }
        }
    }
    return g[endNode]!!
}

class Day20(val lines: List<String>) : AocChallenge(2019, 20) {

    private data class Graph<N>(val graph: Map<N, Map<N, Int>>) {

        fun find(predicate: (N) -> Boolean): N {
            return graph.keys.single(predicate)
        }

        fun edges(vertex: N): Map<N, Int> {
            return graph[vertex]!!
        }
    }

    private data class Position(val x: Int, val y: Int)

    private data class Portal(val label: String, val circleDelta: Int)

    private fun isPortal(y: Int, x: Int, c: Char): String? {
        if (c != '.') {
            return null
        }
        for ((dy, dx) in NSWE) {
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

    private fun findPortals(): Map<Position, Portal> {
        val width = lines.maxOf { it.length }
        val height = lines.size
        val m = mutableMapOf<Position, Portal>()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                isPortal(y, x, c)?.let {label ->
                    if (isOuterPortal(x, y, width, height)) {
                        m[Position(x, y)] = Portal(label, -1)
                    } else {
                        m[Position(x, y)] = Portal(label, +1)
                    }
                }
            }
        }
        return m.toMap()
    }

    private val NSWE = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    private fun neighborPositions(position: Position): Sequence<Position> {
        val (x, y) = position
        return sequence {
            for ((dy, dx) in NSWE) {
                if (lines[y+dy][x+dx] == '.') {
                    yield(Position(x + dx, y + dy))
                }
            }
        }
    }

    private fun findConnectedPortals(portalMap: Map<Position, Portal>, startPosition: Position): Map<Portal, Int> {
        val openHeap = PriorityQueue<ComparableNode<Position>>()
        val closedSet = mutableSetOf<Position>()
        openHeap.add(ComparableNode(0, startPosition))
        val connectedPortals = mutableMapOf<Portal, Int>()
        while (openHeap.isNotEmpty()) {
            val current = openHeap.remove()
            if (current.node in portalMap && current.g > 0) {
                val pp = portalMap[current.node]!!
                connectedPortals[Portal(pp.label, pp.circleDelta)] = current.g
            }
            closedSet.add(current.node)
            for (neighbor in neighborPositions(current.node)) {
                if (closedSet.contains(neighbor)) {
                    continue
                }
                openHeap.add(ComparableNode(current.g + 1, neighbor))
            }
        }
        val startPortal = portalMap[startPosition]!!
        if (startPortal.label != "AA" && startPortal.label != "ZZ") {
            val op = portalMap.values.single { it.label == startPortal.label && it.circleDelta != startPortal.circleDelta }
            connectedPortals[Portal(op.label, op.circleDelta)] = 1
        }
        return connectedPortals
    }

    private fun generateCompactGraph(): Graph<Portal> {
        val portalMap = findPortals()
        val m = portalMap.map { (position, portal) ->
            portal to findConnectedPortals(portalMap, position)
        }.toMap()
        return Graph(m)
    }

    private fun oneSpaceNeighbors(graph: Graph<Portal>, current: Portal): Map<Portal, Int> {
        return graph.edges(current)
    }

    override fun part1(): Int {
        val graph = generateCompactGraph()
        val startPortal = graph.find { it.label == "AA" }
        val endPortal = graph.find { it.label == "ZZ" }
        return dijkstra(startPortal, endPortal) { oneSpaceNeighbors(graph, it) }
    }

    private data class RecursivePortal(val portal: Portal, val circle: Int)

    private fun recursiveSpacesNeighbors(graph: Graph<Portal>, current: RecursivePortal): Map<RecursivePortal, Int> {
        val result = mutableMapOf<RecursivePortal, Int>()
        graph.edges(current.portal).forEach { (target, distance) ->
            if (target.label == current.portal.label) {
                // hop to another level
                if (current.circle + current.portal.circleDelta >= 0) {
                    assert(target.circleDelta == -current.portal.circleDelta)
                    assert(target.label != "AA")
                    assert(target.label != "ZZ")
                    result[RecursivePortal(target, current.circle + current.portal.circleDelta)] = distance
                }
            } else {
                // same level
                if (!(current.circle > 0 && (target.label == "AA" || target.label == "ZZ")) &&
                    !(current.circle == 0 && target.label != "AA" && target.label != "ZZ" && target.circleDelta < 0)) {
                    result[RecursivePortal(target, current.circle)] = distance
                }
            }
        }
        return result
    }

    override fun part2(): Int {
        val graph = generateCompactGraph()
        val startPortal = RecursivePortal(graph.find { it.label == "AA" }, 0)
        val endPortal = RecursivePortal(graph.find { it.label == "ZZ" }, 0)
        return dijkstra(startPortal, endPortal) { recursiveSpacesNeighbors(graph, it) }
    }
}
