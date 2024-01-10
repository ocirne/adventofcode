package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.combinationsOfTwo
import io.github.ocirne.aoc.exclusiveRange
import io.github.ocirne.aoc.gcd
import kotlin.math.*

class Day10(val lines: List<String>) : AocChallenge(2019, 10) {

    data class Asteroid(val x: Int, val y: Int)

    private val asteroids: List<Asteroid> =
        if (lines.isNotEmpty()) readAsteroids(lines) else listOf()

    private fun readAsteroids(lines: List<String>): List<Asteroid> {
        val mutableAsteroids = mutableListOf<Asteroid>()
        lines.mapIndexed { y, line ->
            line.mapIndexed { x, value ->
                if (value == '#') {
                    mutableAsteroids.add(Asteroid(x, y))
                }
            }
        }
        return mutableAsteroids.toList()
    }

    private fun isVisible(a: Asteroid, b: Asteroid): Boolean {
        val dx = b.x - a.x
        val dy = b.y - a.y
        if (dx == 0) {
            return !exclusiveRange(a.y, b.y).any { y -> asteroids.contains(Asteroid(a.x, y)) }
        }
        if (dy == 0) {
            return !exclusiveRange(a.x, b.x).any { x -> asteroids.contains(Asteroid(x, a.y)) }
        }
        val g = gcd(dx.absoluteValue, dy.absoluteValue)
        if (g == 1) {
            return true
        }
        for (i in exclusiveRange(0, g)) {
            val x = a.x + i * dx / g
            val y = a.y + i * dy / g
            if (asteroids.contains(Asteroid(x, y))) {
                return false
            }
        }
        return true
    }

    private fun inc(m: MutableMap<Asteroid, Int>, v: Asteroid) {
        val count = m.getOrDefault(v, 0)
        m[v] = count + 1
    }

    private fun findBestPosition(): Pair<Asteroid, Int> {
        val visibleAsteroids = mutableMapOf<Asteroid, Int>()
        asteroids.combinationsOfTwo().forEach { (a, b) ->
            val v = isVisible(a, b)
            if (v) {
                inc(visibleAsteroids, a)
                inc(visibleAsteroids, b)
            }
        }
        return visibleAsteroids.maxBy { it.value }.toPair()
    }

    override fun part1(): Int {
        val (_, count) = findBestPosition()
        return count
    }

    fun foo(m: Asteroid, a: Asteroid): Pair<Int, Double> {
        val x = m.x - a.x
        val y = m.y - a.y
        val r = sqrt((x * x + y * y).toDouble())
        var phi = if (y >= 0) {
            acos(x / r) + 3 * PI / 2
        } else {
            2 * PI - acos (x / r) + 3 * PI / 2
        }
        if (phi >= 2*PI) {
            phi -= 2*PI
        }
        val roundedPhi = (10000.0 * phi).toInt()
        return roundedPhi to r
    }

    override fun part2(): Int {
        val (monitoringStation, _) = findBestPosition()
        val m = mutableMapOf<Int, MutableList<Pair<Double, Asteroid>>>()
        for (asteroid in asteroids) {
            if (asteroid == monitoringStation) {
                continue
            }
            val (phi, r) = foo(monitoringStation, asteroid)
            if (!m.contains(phi)) {
                m[phi] = mutableListOf()
            }
            m[phi]!!.add(r to asteroid)
        }
        var i = 0
        var level = 0
        while (true) {
            for ((_, rs) in m.toSortedMap()) {
                if (level < rs.size) {
                    i += 1
                }
                if (i == 200) {
                    val t = rs.sortedBy { it.first }.get(level).second
                    return 100 * t.x + t.y
                }
            }
            level ++
        }
    }
}
