package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.absoluteValue

class Day12(val lines: List<String>) : AocChallenge(2019, 12) {

    companion object {
        private val MOON_PATTERN = """<x=(-?\d+), y=(-?\d+), z=(-?\d+)>""".toRegex()
    }

    data class Vector(val x: Int, val y: Int, val z: Int) {

        operator fun plus(o: Vector): Vector = Vector(x + o.x, y + o.y, z + o.z)

        fun getEnergy(): Int = x.absoluteValue + y.absoluteValue + z.absoluteValue

    }

    data class Moon(var position: Vector, var velocity: Vector) {

        fun applyVelocity(): Moon = Moon(position + velocity, velocity)

        fun getTotalEnergy(): Int = position.getEnergy() * velocity.getEnergy()
    }

    fun foo(steps: Int): Int {
        var moons = lines.map { line ->
            val (px, py, pz) = MOON_PATTERN.find(line)!!.destructured
            Moon(Vector(px.toInt(), py.toInt(), pz.toInt()), Vector(0, 0, 0))
        }
        IntRange(1, steps).forEach { _ ->
            // gravity
            moons = moons.map { moon ->
                var nx = 0
                var ny = 0
                var nz = 0
                moons.forEach { otherMoon ->
                    nx += otherMoon.position.x.compareTo(moon.position.x)
                    ny += otherMoon.position.y.compareTo(moon.position.y)
                    nz += otherMoon.position.z.compareTo(moon.position.z)
                }
                Moon(moon.position, moon.velocity + Vector(nx, ny, nz))
            }
            // velocity
            moons = moons.map(Moon::applyVelocity)
        }
        return moons.sumOf { it.getTotalEnergy() }
    }

    override fun part1(): Int {
        return foo(1000)
    }

    private fun readMoons(): List<Moon> {
        return lines.map { line ->
            val (px, py, pz) = MOON_PATTERN.find(line)!!.destructured
            Moon(Vector(px.toInt(), py.toInt(), pz.toInt()), Vector(0, 0, 0))
        }
    }

    data class SingleMoon(var position: Int, var velocity: Int) {

        fun addVelocity(delta: Int) {
            velocity += delta
        }
        fun applyVelocity() {
            position += velocity
        }
    }

    private fun simulate(moons: List<SingleMoon>): Long {
        var index = 0L
        val seen = mutableMapOf<String, Long>()
        while (true) {
            val key = moons.toString()
            if (seen.contains(key)) {
                assert(seen[key] == 0L)
                return index
            }
            seen[key] = index
            index++
            // gravity
            moons.forEach { moon ->
                var delta = 0
                moons.forEach { otherMoon ->
                    delta += otherMoon.position.compareTo(moon.position)
                }
                moon.addVelocity(delta)
            }
            // velocity
            moons.forEach(SingleMoon::applyVelocity)
        }
    }

    private fun gcd(a: Long, b: Long): Long {
        return if (b > 0) gcd(b, a % b) else a
    }

    private fun lcm(a: Long, b: Long): Long {
        return a / gcd(a, b) * b
    }

    override fun part2(): Long {
        val moons = readMoons()
        val mx = simulate(moons.map { moon -> SingleMoon(moon.position.x, moon.velocity.x) })
        val my = simulate(moons.map { moon -> SingleMoon(moon.position.y, moon.velocity.y) })
        val mz = simulate(moons.map { moon -> SingleMoon(moon.position.z, moon.velocity.z) })
        return listOf(mx, my, mz).reduce { acc, v -> lcm(acc, v) }
    }
}
