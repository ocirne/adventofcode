package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.lang.Integer.compare
import kotlin.math.absoluteValue

class Day12(val lines: List<String>) : AocChallenge(2019, 12) {

    private val MOON_PATTERN = """<x=(-?\d+), y=(-?\d+), z=(-?\d+)>""".toRegex()

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
        IntRange(1, steps).forEach {
            // gravity
            moons = moons.map { moon ->
                var nx = 0
                var ny = 0
                var nz = 0
                moons.forEach { otherMoon ->
                    if (moon != otherMoon) {
                        nx += otherMoon.position.x.compareTo(moon.position.x)
                        ny += otherMoon.position.y.compareTo(moon.position.y)
                        nz += otherMoon.position.z.compareTo(moon.position.z)
                    }
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

    override fun part2(): Int {
        return -1
    }
}
