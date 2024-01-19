package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.util.PriorityQueue

class Day15(val lines: List<String>) : AocChallenge(2019, 15) {

    private class Droid(val program: String) {

        data class Position(val x: Int, val y: Int)

        class Node(val steps: Int, val position: Position, val program: IntCodeEmulator2019): Comparable<Node> {
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
                            yield(Node(steps + 1, Position(x + dx, y - dy), copy))
                        }
                    }
                }
            }

            override fun compareTo(other: Node): Int {
                return steps.compareTo(other.steps)
            }
        }

        fun exploreMap(): Node {
            val openHeap = PriorityQueue<Node>()
            val visited = mutableSetOf<Position>()
            openHeap.add(Node(0, Position(0, 0), IntCodeEmulator2019(program)))
            while (openHeap.isNotEmpty()) {
                val node = openHeap.remove()
                if (node.isEnd()) {
                    return node
                }
                visited.add(node.position)
                for (neighbor in node.neighbors()) {
                    if (visited.contains(neighbor.position)) {
                        continue
                    }
                    openHeap.add(neighbor)
                }
            }
            throw IllegalStateException()
        }

        fun fillMap2(node: Node): Int {
            val openHeap = PriorityQueue<Node>()
            val visited = mutableMapOf<Position, Int>()
            openHeap.add(Node(0, node.position, node.program))
            while (openHeap.isNotEmpty()) {
                val node = openHeap.remove()
                visited[node.position] = node.steps
                for (neighbor in node.neighbors()) {
                    if (visited.contains(neighbor.position)) {
                        continue
                    }
                    openHeap.add(neighbor)
                }
            }
            return visited.values.max()
        }
    }

    override fun part1(): Int {
        return Droid(lines.first()).exploreMap().steps
    }

    override fun part2(): Int {
        val oxygenSystem = Droid(lines.first()).exploreMap()
        return Droid(lines.first()).fillMap2(oxygenSystem)
    }
}
