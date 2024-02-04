package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.ComparableNode
import io.github.ocirne.aoc.NSWE
import io.github.ocirne.aoc.dijkstra
import io.github.ocirne.aoc.year2019.NodeType.*
import java.util.*

private enum class NodeType { KEY, DOOR }

private data class Node(val label: Char, val type: NodeType)


private typealias VaultGraph = Map<Node, Map<Node, Int>>

class Day18(val lines: List<String>) : AocChallenge(2019, 18) {

    private data class Position(val x: Int, val y: Int)

    private fun findKeyAndDoors(): Map<Position, Node> {
        val m = mutableMapOf<Position, Node>()
        var i = 1
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                when {
                    c == '@' -> m[Position(x, y)] = Node((i++).digitToChar(), KEY)
                    c.isLowerCase() -> m[Position(x, y)] = Node(c, KEY)
                    c.isUpperCase() -> m[Position(x, y)] = Node(c.lowercaseChar(), DOOR)
                }
            }
        }
        return m.toMap()
    }

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
        val nodeMap = findKeyAndDoors()
        return nodeMap.map { (position, startNode) -> startNode to findConnectedNodes(nodeMap, position) }.toMap()
    }

    private fun reachableKeys(graph: VaultGraph, startKey: Char, hiddenKeys: Set<Char>): Sequence<Pair<Char, Int>> {
        return sequence {
            val openHeap = PriorityQueue<ComparableNode<Node>>()
            val closedSet = mutableSetOf<Node>()
            openHeap.add(ComparableNode(0, Node(startKey, type=KEY)))
            while (openHeap.isNotEmpty()) {
                val current = openHeap.remove()
                val node = current.node
                closedSet.add(current.node)
                if (node.type == KEY && node.label in hiddenKeys) {
                    yield(node.label to current.g)
                } else if (node.type == DOOR && node.label in hiddenKeys) {
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

    private data class KeyPathNode(val droids: Set<Char>, val hiddenKeys: Set<Char>)

    private fun reachableKeys(graph: VaultGraph, keyPathNode: KeyPathNode): Sequence<Pair<KeyPathNode, Int>> {
        return sequence {
            for (label in keyPathNode.droids) {
                for ((k, d) in reachableKeys(graph, label, keyPathNode.hiddenKeys)) {
                    yield(KeyPathNode(keyPathNode.droids - label + k, keyPathNode.hiddenKeys - k) to d)
                }
            }
        }
    }

    override fun part1(): Int {
        val graph = generateVaultGraph()
        val startKeys = setOf('1')
        val totalKeys = graph.filter { (k, _) -> k.type == KEY }.map { it.key.label }.toSet()
        return dijkstra(KeyPathNode(startKeys, totalKeys - startKeys),
            { g, node -> node.hiddenKeys.isEmpty() },
            { reachableKeys(graph, it) })
    }

    override fun part2(): Int {
        val graph = generateVaultGraph()
        val startKeys = setOf('1', '2', '3', '4')
        val totalKeys = graph.filter { (k, _) -> k.type == KEY }.map { it.key.label }.toSet()
        return dijkstra(KeyPathNode(startKeys, totalKeys - startKeys),
            { g, node -> node.hiddenKeys.isEmpty() },
            { reachableKeys(graph, it) })
    }
}
