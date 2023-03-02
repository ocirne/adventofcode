package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge
import java.util.*

typealias Position = Pair<Int, Int>

val oldest: Comparator<Pair<Int, Position>> = compareBy { it.first }

class Day24(val lines: List<String>) : AocChallenge(2022, 24) {

    fun findNeighbors(afoo: Map<Int, Set<Position>>, minute: Int, position: Position): List<Position> {
        println("minute $minute")
        val walls = afoo[minute]!!
        val result = mutableListOf<Position>()
        val (x, y) = position
        for (p in listOf(Position(x - 1, y), Position(x + 1, y), Position(x, y - 1), Position(x, y + 1))) {
            if (p !in walls) {
                result.add(p)
            }
        }
        return result
    }

    fun dijkstra(afoo: Map<Int, Set<Position>>, start: Position, end: Position, minute_0:Int=0): Int {
        val openHeap = PriorityQueue<Pair<Int, Position>>(oldest)
        val closedSet = mutableSetOf<Pair<Int, Position>>()
        openHeap.add(Pair(minute_0, start))
        while (openHeap.isNotEmpty()) {
            val (minute, position) = openHeap.remove()
            if (position == end) {
                return minute - minute_0
            }
            if (Pair(minute, position) in closedSet) {
                continue
            }
            closedSet.add(Pair(minute, position))
            for (neighbor in findNeighbors(afoo, minute, position)) {
                openHeap.add(Pair(minute + 1, neighbor))
            }
        }
        throw RuntimeException("No solution")
    }

    fun atMinute(foo: Map<Position, Char>, minute: Int): Set<Position> {
        return foo.map { (pos, t) ->
            val (x, y) = pos
//            if (pos == Position(5, 1)) {
//                println(Position(x, (y-1 - minute + 4).mod(4) + 1))
//            }
            when (t) {
                '#' -> pos
                '<' -> Position((x-1 - minute).mod(6) + 1, y)
                '>' -> Position((x-1 + minute).mod(6) + 1, y)
                '^' -> Position(x, (y-1 - minute).mod(4) + 1)
                'v' -> Position(x, (y-1 + minute).mod(4) + 1)
                else -> throw IllegalArgumentException("$pos $t")
            }
        }.toSet()
    }

    fun allMinutes(foo: Map<Position, Char>): Map<Int, Set<Position>> {
        return (0..1000).associateWith { m -> atMinute(foo, m) }
    }

    fun printWalls(walls: Set<Position>) {
        for (y in 0..10) {
            for (x in 0.. 10) {
                if (Position(x, y) in walls) {
                    print('#')
                } else {
                    print('.')
                }
            }
            println()
        }
    }

    override fun part1(): Int {
        val foo = lines.flatMapIndexed { y, line -> line.mapIndexed { x, t -> Pair(x, y) to t } }.filter { (_, t) -> t != '.' }.toMap()
        val afoo = allMinutes(foo)
        return dijkstra(afoo, start=Position(1, 0), end=Position(6, 5))
    }

    override fun part2(): Int {
        val foo = lines.flatMapIndexed { y, line -> line.mapIndexed { x, t -> Pair(x, y) to t } }.filter { (_, t) -> t != '.' }.toMap()
        val afoo = allMinutes(foo)
        val m1 = dijkstra(afoo, start=Position(1, 0), end=Position(6, 5))
        val m2 = dijkstra(afoo, start=Position(6, 5), end=Position(1, 0), m1)
        val m3 = dijkstra(afoo, start=Position(1, 0), end=Position(6, 5), m1+ m2)
        return m1 + m2 + m3
    }
}
