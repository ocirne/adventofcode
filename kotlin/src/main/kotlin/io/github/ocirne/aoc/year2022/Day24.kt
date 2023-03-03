package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge
import java.util.*

typealias Position = Pair<Int, Int>

val oldest: Comparator<Pair<Int, Position>> = compareBy { it.first }

class Day24(val lines: List<String>) : AocChallenge(2022, 24) {

    private val initialMap = createInitialMap()

    private val allMaps = mutableMapOf<Int, Set<Position>>()

    private val width = if (lines.isNotEmpty()) lines.first().length else 0

    private val height = lines.size

    private val start = Position(1, 0)

    private val end = Position(width-2, height-1)

    private fun createInitialMap(): Map<Position, Char> {
        return lines.flatMapIndexed { y, line -> line.mapIndexed { x, t -> Pair(x, y) to t } }
            .filter { (_, t) -> t != '.' }.toMap()
    }

    private fun atMinute(minute: Int): Set<Position> {
        return initialMap.map { (pos, t) ->
            val (x, y) = pos
            when (t) {
                '#' -> pos
                '<' -> Position((x-1 - minute).mod(width-2) + 1, y)
                '>' -> Position((x-1 + minute).mod(width-2) + 1, y)
                '^' -> Position(x, (y-1 - minute).mod(height-2) + 1)
                'v' -> Position(x, (y-1 + minute).mod(height-2) + 1)
                else -> throw IllegalArgumentException("$pos $t")
            }
        }.toSet()
    }

    private fun findNeighbors(minute: Int, position: Position): List<Position> {
        val walls = allMaps.computeIfAbsent(minute) { atMinute(it + 1) }
        val (x, y) = position
        return listOf(position, Position(x - 1, y), Position(x + 1, y), Position(x, y - 1), Position(x, y + 1))
            .filter { p -> p.first in 0 .. width && p.second in 0 .. height }
            .filter { p -> p !in walls }
    }

    private fun dijkstra(start: Position, end: Position, minute_0:Int=0): Int {
        val openHeap = PriorityQueue(oldest)
        val closedSet = mutableSetOf<Pair<Int, Position>>()
        openHeap.add(Pair(minute_0, start))
        while (openHeap.isNotEmpty()) {
            val (minute, position) = openHeap.remove()
            if (position == end) {
                return minute
            }
            if (Pair(minute, position) in closedSet) {
                continue
            }
            closedSet.add(Pair(minute, position))
            for (neighbor in findNeighbors(minute, position)) {
                openHeap.add(Pair(minute + 1, neighbor))
            }
        }
        throw RuntimeException()
    }

    override fun part1(): Int {
        return dijkstra(start=start, end=end)
    }

    override fun part2(): Int {
        val m1 = dijkstra(start=start, end=end)
        val m2 = dijkstra(start=end, end=start, m1)
        return dijkstra(start=start, end=end, m2)
    }
}
