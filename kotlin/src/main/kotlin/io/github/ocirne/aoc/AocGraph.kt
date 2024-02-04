package io.github.ocirne.aoc

import java.util.*

val NSWE = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

class ComparableNode<N>(val g: Int, val node: N): Comparable<ComparableNode<N>> {

    override fun compareTo(other: ComparableNode<N>): Int {
        return g.compareTo(other.g)
    }
}

fun <N> dijkstra(startNode: N,
                 endCondition: (Int, N) -> Boolean,
                 neighbors: (N) -> Sequence<Pair<N, Int>>): Int {
    val openHeap = PriorityQueue<ComparableNode<N>>()
    val closedSet = mutableSetOf<N>()
    val g = mutableMapOf(startNode to 0)
    openHeap.add(ComparableNode(0, startNode))
    while (openHeap.isNotEmpty()) {
        val current = openHeap.remove()
        if (endCondition(current.g, current.node)) {
            return current.g
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
    return -1
}
