package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.util.PriorityQueue

class Day15(val lines: List<String>) : AocChallenge(2019, 15) {

    private data class Position(val x: Int, val y: Int)

    private class Node(val steps: Int, val position: Position, val program: IntCodeEmulator2019): Comparable<Node> {
        fun isEnd(): Boolean {
            return steps > 0 && program.getLastOutput() == 2L
        }

        fun neighbors(): Sequence<Node> {
            val (x, y) = position
            return sequence {
                for ((direction, dx, dy) in listOf(
                    Triple(1L, 0, -1),
                    Triple(2L, 0, 1),
                    Triple(3L, -1, 0),
                    Triple(4L, 1, 0),
                )) {
                    val copy = program.copy()
                    copy.addInput(direction)
                    copy.tick()
                    if (copy.getLastOutput() != 0L) {
                        yield(Node(steps + 1, Position(x + dx, y + dy), copy))
                    }
                }
            }
        }

        override fun compareTo(other: Node): Int {
            return steps.compareTo(other.steps)
        }
    }

    private fun exploreMap(startNode: Node): Node {
        val openHeap = PriorityQueue<Node>()
        val visited = mutableMapOf<Position, Node>()
        openHeap.add(Node(0, startNode.position, startNode.program))
        while (openHeap.isNotEmpty()) {
            val node = openHeap.remove()
            if (node.isEnd()) {
                return node
            }
            visited[node.position] = node
            for (neighbor in node.neighbors()) {
                if (visited.contains(neighbor.position)) {
                    continue
                }
                openHeap.add(neighbor)
            }
        }
        return visited.values.maxBy { it.steps }
    }

    private fun findOxygenSystem(): Node {
        val startNode = Node(0, Position(0, 0), IntCodeEmulator2019(lines.first()))
        return exploreMap(startNode)
    }

    override fun part1(): Int {
        return findOxygenSystem().steps
    }

    override fun part2(): Int {
        val oxygenSystem = findOxygenSystem()
        return exploreMap(oxygenSystem).steps
    }
}
