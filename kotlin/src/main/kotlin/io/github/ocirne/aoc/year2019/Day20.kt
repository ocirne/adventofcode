package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.ComparableNode
import io.github.ocirne.aoc.NSWE
import io.github.ocirne.aoc.dijkstra
import java.util.*

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

    private fun oneSpaceNeighbors(graph: Graph<Portal>, current: Portal): Sequence<Pair<Portal, Int>> {
        return sequence {
            for ((portal, distance) in graph.edges(current)) {
                yield(portal to distance)
            }
        }
    }

    override fun part1(): Int {
        val graph = generateCompactGraph()
        val startPortal = graph.find { it.label == "AA" }
        val endPortal = graph.find { it.label == "ZZ" }
        return dijkstra(startPortal,
            { _, node -> node == endPortal },
            { oneSpaceNeighbors(graph, it) })
    }

    private data class RecursivePortal(val portal: Portal, val circle: Int)

    private fun recursiveSpacesNeighbors(graph: Graph<Portal>, current: RecursivePortal): Sequence<Pair<RecursivePortal, Int>> {
        return sequence {
            graph.edges(current.portal).forEach { (target, distance) ->
                if (target.label == current.portal.label) {
                    // hop to another level
                    if (current.circle + current.portal.circleDelta >= 0) {
                        assert(target.circleDelta == -current.portal.circleDelta)
                        assert(target.label != "AA")
                        assert(target.label != "ZZ")
                        yield(RecursivePortal(target, current.circle + current.portal.circleDelta) to distance)
                    }
                } else {
                    // same level
                    if (!(current.circle > 0 && (target.label == "AA" || target.label == "ZZ")) &&
                        !(current.circle == 0 && target.label != "AA" && target.label != "ZZ" && target.circleDelta < 0)
                    ) {
                        yield(RecursivePortal(target, current.circle) to distance)
                    }
                }
            }
        }
    }

    override fun part2(): Int {
        val graph = generateCompactGraph()
        val startPortal = RecursivePortal(graph.find { it.label == "AA" }, 0)
        val endPortal = RecursivePortal(graph.find { it.label == "ZZ" }, 0)
        return dijkstra(startPortal,
            { _, node -> node == endPortal },
            { recursiveSpacesNeighbors(graph, it) })
    }
}
