package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge
import java.util.*

typealias Position = Pair<Int, Int>

data class MinutePosition(val minute: Int, val x: Int, val y: Int) {

    constructor(minute: Int, p: Position) : this(minute, p.first, p.second)

    fun position(): Position {
        return Position(x, y)
    }

    fun move(dx: Int, dy: Int): MinutePosition {
        return MinutePosition(minute + 1, x + dx, y + dy)
    }
}

val oldest: Comparator<MinutePosition> = compareBy { it.minute }

class Day24(val lines: List<String>) : AocChallenge(2022, 24) {

    private val initialMap = createInitialMap()

    private val allMaps = mutableMapOf<Int, Set<Position>>()

    private val width = if (lines.isNotEmpty()) lines.first().length else 0

    private val height = lines.size

    private val start = Position(1, 0)

    private val end = Position(width - 2, height - 1)

    private val movements: List<Position> = listOf(Pair(0, 0), Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))

    private fun createInitialMap(): Map<Position, Char> {
        return lines.flatMapIndexed { y, line -> line.mapIndexed { x, t -> Pair(x, y) to t } }
            .filter { (_, t) -> t != '.' }.toMap()
    }

    private fun atMinute(minute: Int): Set<Position> {
        return initialMap.map { (pos, t) ->
            val (x, y) = pos
            when (t) {
                '#' -> pos
                '<' -> Position((x - 1 - minute).mod(width - 2) + 1, y)
                '>' -> Position((x - 1 + minute).mod(width - 2) + 1, y)
                '^' -> Position(x, (y - 1 - minute).mod(height - 2) + 1)
                'v' -> Position(x, (y - 1 + minute).mod(height - 2) + 1)
                else -> throw IllegalArgumentException("$pos $t")
            }
        }.toSet()
    }

    private fun findNeighbors(current: MinutePosition): List<MinutePosition> {
        val walls = allMaps.computeIfAbsent(current.minute + 1) { atMinute(it) }
        return movements
            .map { (dx, dy) -> current.move(dx, dy) }
            .filter { it.x in 0..width && it.y in 0..height }
            .filter { it.position() !in walls }
    }

    private fun dijkstra(start: Position, end: Position, minute_0: Int = 0): Int {
        val openHeap = PriorityQueue(oldest)
        val closedSet = mutableSetOf<MinutePosition>()
        openHeap.add(MinutePosition(minute_0, start))
        while (openHeap.isNotEmpty()) {
            val current = openHeap.remove()
            if (current.position() == end) {
                return current.minute
            }
            if (current in closedSet) {
                continue
            }
            closedSet.add(current)
            for (neighbor in findNeighbors(current)) {
                openHeap.add(neighbor)
            }
        }
        throw RuntimeException()
    }

    override fun part1(): Int {
        return dijkstra(start = start, end = end)
    }

    override fun part2(): Int {
        val m1 = dijkstra(start = start, end = end)
        val m2 = dijkstra(start = end, end = start, m1)
        return dijkstra(start = start, end = end, m2)
    }
}
