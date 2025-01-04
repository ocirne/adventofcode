package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.ComparableNode
import io.github.ocirne.aoc.dijkstra
import java.util.*

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

    private data class CostableNode(val node: Node, val cost: Int)

    private fun dijkstraWithParents(startNode: Node,
                                    endCondition: (Int, Node) -> Boolean,
                                    neighbors: (Node) -> Sequence<Pair<Node, Int>>): Map<CostableNode, Set<CostableNode>> {
        val openHeap = PriorityQueue<ComparableNode<Node>>()
        val closedSet = mutableSetOf<Node>()
        var endCost: Int? = null
        val g = mutableMapOf(startNode to 0)
        val parent = mutableMapOf<CostableNode, MutableSet<CostableNode>>()
        openHeap.add(ComparableNode(0, startNode))
        while (openHeap.isNotEmpty()) {
            val current = openHeap.remove()
            if (endCost != null && current.g >= endCost) {
                continue
            }
            if (endCondition(current.g, current.node)) {
                println(current.g)
                endCost = current.g
            }
            closedSet.add(current.node)
            for ((neighborNode, distance) in neighbors(current.node)) {
                val tg = g[current.node]!! + distance
                if (neighborNode in closedSet && tg >= g[neighborNode]!!) {
                    continue
                }
                if (tg <= g.getOrDefault(neighborNode, 0) || ! openHeap.map { it.node }.contains(neighborNode)) {
                    g[neighborNode] = tg
                    val pn = CostableNode(neighborNode, tg)
                    if (!parent.contains(pn)) {
                        parent[pn] = mutableSetOf()
                    }
                    parent[pn]!!.add(CostableNode(current.node, current.g))
                    openHeap.add(ComparableNode(tg, neighborNode))
                }
            }
        }
        return parent.filter { it.key.cost <= endCost!! }
    }

    private fun retraceParents(parents: Map<CostableNode, Set<CostableNode>>, endPosition: Position): Set<Position> {
        val openList = mutableListOf<CostableNode>()
        val bestPaths = mutableSetOf<Position>()
        val maxCost = parents.keys.maxOf { it.cost }
        for (d in "^v<>") {
            openList.add(CostableNode(Node(endPosition, d), maxCost))
        }
        while (openList.isNotEmpty()) {
            val current = openList.removeFirst()
            bestPaths.add(current.node.position)
            if (!parents.contains(current)) {
                continue
            }
            for (parent in parents[current]!!) {
                openList.add(parent)
            }
        }
        return bestPaths
    }

    override fun part2(): Int {
        val grid = readGrid()
        val startNode = Node(findPosition(grid, 'S'), '>')
        val endPosition = findPosition(grid, 'E')
        val parents = dijkstraWithParents(startNode,
            endCondition = { _, node -> node.position == endPosition },
            neighbors = { position -> oneSpaceNeighbors(grid, position) })
        val bestPaths = retraceParents(parents, endPosition)
        for (y in 0 .. 140) {
            for (x in 0..140) {
                val p = Position(x, y)
                when {
                    // TODO
                   (p in bestPaths) -> print('O')
                    (p in grid) -> print(grid[p])
                    else -> print(' ')
                }
            }
            println()
        }
        return bestPaths.size
    }
}
