package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.combinationsOfTwo
import kotlin.math.abs

class Day14(val lines: List<String>, val width: Int, val height: Int) : AocChallenge(2024, 14) {

    constructor(lines: List<String>) : this(lines, width = 101, height = 103)

    private val startPosition = Regex("p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)")

    private val hw = (width - 1) / 2
    private val hh = (height - 1) / 2
    private val seconds = 100

    private data class Point(val x: Int, val y: Int)

    private data class Robot(val p: Point, val v: Point)

    private fun readRobots(): List<Robot> {
        return lines.map { line ->
            val (px, py, vx, vy) = startPosition.find(line)!!.destructured
            Robot(Point(px.toInt(), py.toInt()), Point(vx.toInt(), vy.toInt()))
        }
    }

    private fun findDestinations(robots: List<Robot>, seconds: Int): List<Point> {
        return robots.map { (p, v) ->
            val ex = (p.x + seconds.mod(width) * v.x).mod(width)
            val ey = (p.y + seconds.mod(height) * v.y).mod(height)
            Point(ex, ey)
        }
    }

    override fun part1(): Int {
        val destinations = findDestinations(readRobots(), seconds)
        val q1 = destinations.count { (x, y) -> x < hw && y < hh }
        val q2 = destinations.count { (x, y) -> x < hw && y > hh }
        val q3 = destinations.count { (x, y) -> x > hw && y < hh }
        val q4 = destinations.count { (x, y) -> x > hw && y > hh }
        return q1 * q2 * q3 * q4
    }

    private fun countDistanceOne(destinations: List<Point>): Int {
        return destinations.combinationsOfTwo().map { (f, s) ->
            Point(abs(f.x - s.x), abs(f.y - s.y))
        }.filter { (dx, dy) -> dx < 1 || dy < 1 }.count()
    }

    private fun printlnTree(destinations: Set<Point>) {
        for (y in 0 until height) {
            for (x in 0 until width) {
                print(if (destinations.contains(Point(x, y))) '#' else '.')
            }
            println()
        }
    }

    override fun part2(): Int {
        val robots = readRobots()
        // step 101 found by trial and error
        for (s in 230 until 10000 step 101) {
            val destinations = findDestinations(robots, s)
            val c = countDistanceOne(destinations)
            // threshold 5000 found by trial and error
            if (c > 5000) {
                printlnTree(destinations.toSet())
                return s
            }
        }
        return -1
    }
}
