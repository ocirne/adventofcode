package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.year2019.NodeType.*
import java.util.*

private enum class NodeType { START, KEY, DOOR }

private data class Node(val label: Char, val type: NodeType)


private typealias VaultGraph = Map<Node, Map<Node, Int>>

class Day18(val lines: List<String>) : AocChallenge(2019, 18) {

    private class ComparableNode<N>(val g: Int, val node: N): Comparable<ComparableNode<N>> {

        override fun compareTo(other: ComparableNode<N>): Int {
            return g.compareTo(other.g)
        }
    }

    private data class KeyPathNode(val label: Char, val foundKeys: Set<Char>)

    private data class Position(val x: Int, val y: Int)

    private fun findNodes(): Map<Position, Node> {
        val m = mutableMapOf<Position, Node>()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                when {
                    c == '@' -> m[Position(x, y)] = Node(c, KEY)
                    c.isLowerCase() -> m[Position(x, y)] = Node(c, KEY)
                    c.isUpperCase() -> m[Position(x, y)] = Node(c.lowercaseChar(), DOOR)
                }
            }
        }
        return m.toMap()
    }

    private val NSWE = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    private fun neighborPositions(current: Position): Sequence<Position> {
        val (x, y) = current
        return sequence {
            for ((dy, dx) in NSWE) {
                if (lines[y+dy][x+dx] != '#') {
                    yield(Position(x + dx, y + dy))
                }
            }
        }
    }

    private fun findConnectedNodes(positionMap: Map<Position, Node>, startPosition: Position): Map<Node, Int> {
        val openHeap = PriorityQueue<ComparableNode<Position>>()
        val closedSet = mutableSetOf<Position>()
        openHeap.add(ComparableNode(0, startPosition))
        val connectedNodes = mutableMapOf<Node, Int>()
        while (openHeap.isNotEmpty()) {
            val current = openHeap.remove()
            if (closedSet.contains(current.node)) {
                continue
            }
            closedSet.add(current.node)
            if (current.node in positionMap && current.g > 0) {
                val connectedNode = positionMap[current.node]!!
                assert(!connectedNodes.contains(connectedNode))
                connectedNodes[connectedNode] = current.g
            } else {
                for (neighborPosition in neighborPositions(current.node)) {
                    if (closedSet.contains(neighborPosition)) {
                        continue
                    }
                    openHeap.add(ComparableNode(current.g + 1, neighborPosition))
                }
            }
        }
        return connectedNodes
    }

    private fun generateVaultGraph(): VaultGraph {
        val nodeMap = findNodes()
        return nodeMap.map { (position, startNode) -> startNode to findConnectedNodes(nodeMap, position) }.toMap()
    }

    private fun reachableKeys(graph: VaultGraph, keyPathNode: KeyPathNode): Sequence<Pair<KeyPathNode, Int>> {
        return sequence {
            val openHeap = PriorityQueue<ComparableNode<Node>>()
            val closedSet = mutableSetOf<Node>()
            openHeap.add(ComparableNode(0, Node(keyPathNode.label, type=KEY)))
            while (openHeap.isNotEmpty()) {
                val current = openHeap.remove()
                val node = current.node
                closedSet.add(current.node)
                if (node.type == KEY && node.label !in keyPathNode.foundKeys) {
                    val nextNode = KeyPathNode(node.label, keyPathNode.foundKeys + node.label)
                    yield(nextNode to current.g)
                } else if (node.type == DOOR && node.label !in keyPathNode.foundKeys) {
                    // closed door, do not proceed
                } else {
                    for ((neighborNode, distance) in graph.getValue(current.node)) {
                        if (neighborNode in closedSet) {
                            continue
                        }
                        openHeap.add(ComparableNode(current.g + distance, neighborNode))
                    }
                }
            }
        }
    }

    private fun navigateVault(graph: VaultGraph, startKeyPathNode: KeyPathNode): Int {
        val totalKeys = graph.filter { (k, _) -> k.type == KEY }.size
        val openHeap = PriorityQueue<ComparableNode<KeyPathNode>>()
        val closedSet = mutableSetOf<KeyPathNode>()
        val g = mutableMapOf(startKeyPathNode to 0)
        openHeap.add(ComparableNode(0, startKeyPathNode))
        while (openHeap.isNotEmpty()) {
            val current = openHeap.remove()
            println("heap ${openHeap.size}, g ${current.g}, pos ${current.node} keys ${current.node.foundKeys} total ${totalKeys}")
            if (totalKeys == current.node.foundKeys.size) {
                return current.g
            }
            closedSet.add(current.node)
            for ((neighborKeyNode, distance) in reachableKeys(graph, current.node)) {
                val tg = g[current.node]!! + distance
                if (neighborKeyNode in closedSet && tg >= g[neighborKeyNode]!!) {
                    continue
                }
                if (tg < g.getOrDefault(neighborKeyNode, 0) || !openHeap.map { it.node }.contains(neighborKeyNode)) {
                    g[neighborKeyNode] = tg
                    openHeap.add(ComparableNode(tg, neighborKeyNode))
                }
            }
        }
        return -1
    }

    override fun part1(): Int {
        val graph = generateVaultGraph()
        for ((n, es) in graph) {
            println("$n:")
            for ((e, d) in es) {
                println("  $e: $d")
            }
            println()
        }
        return navigateVault(graph, KeyPathNode('@', setOf('@')))
    }

    override fun part2(): Int {
        return -1
    }
}