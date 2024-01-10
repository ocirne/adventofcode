package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.lcmList
import kotlin.math.absoluteValue

class Day12(val lines: List<String>) : AocChallenge(2019, 12) {

    companion object {
        private val MOON_PATTERN = """<x=(-?\d+), y=(-?\d+), z=(-?\d+)>""".toRegex()
    }

    private fun readMoons(): List<Moon> {
        return lines.map { line ->
            val (px, py, pz) = MOON_PATTERN.find(line)!!.destructured
            Moon(Vector(px.toInt(), py.toInt(), pz.toInt()), Vector(0, 0, 0))
        }
    }

    data class Vector(val x: Int, val y: Int, val z: Int) {

        operator fun plus(o: Vector): Vector = Vector(x + o.x, y + o.y, z + o.z)

        fun getEnergy(): Int = x.absoluteValue + y.absoluteValue + z.absoluteValue
    }

    data class Moon(var position: Vector, var velocity: Vector) {

        fun addVelocity(delta: Vector) {
            velocity += delta
        }

        fun applyVelocity() {
            position += velocity
        }

        fun getTotalEnergy(): Int {
            return position.getEnergy() * velocity.getEnergy()
        }
    }

    fun simulateMoons(steps: Int): Int {
        val moons = readMoons()
        IntRange(1, steps).forEach { _ ->
            // gravity
            moons.forEach { moon ->
                val dx = moons.sumOf { otherMoon -> otherMoon.position.x.compareTo(moon.position.x) }
                val dy = moons.sumOf { otherMoon -> otherMoon.position.y.compareTo(moon.position.y) }
                val dz = moons.sumOf { otherMoon -> otherMoon.position.z.compareTo(moon.position.z) }
                moon.addVelocity(Vector(dx, dy, dz))
            }
            // velocity
            moons.forEach(Moon::applyVelocity)
        }
        return moons.sumOf { it.getTotalEnergy() }
    }

    override fun part1(): Int {
        return simulateMoons(1000)
    }

    data class SingleDimension(var position: Int, var velocity: Int) {

        fun addVelocity(delta: Int) {
            velocity += delta
        }
        fun applyVelocity() {
            position += velocity
        }
    }

    private fun findCycleCount(moons: List<SingleDimension>): Long {
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
                moon.addVelocity(moons.sumOf { otherMoon -> otherMoon.position.compareTo(moon.position) })
            }
            // velocity
            moons.forEach(SingleDimension::applyVelocity)
        }
    }

    override fun part2(): Long {
        val moons = readMoons()
        val ix = findCycleCount(moons.map { moon -> SingleDimension(moon.position.x, moon.velocity.x) })
        val iy = findCycleCount(moons.map { moon -> SingleDimension(moon.position.y, moon.velocity.y) })
        val iz = findCycleCount(moons.map { moon -> SingleDimension(moon.position.z, moon.velocity.z) })
        return listOf(ix, iy, iz).lcmList()
    }
}
