package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.combinationsOfTwo
import kotlin.math.abs

class Day14(val lines: List<String>) : AocChallenge(2024, 14) {

    private val start_position = Regex("p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)")

    private val width = 101 // 11
    private val hw = (width-1) / 2
    private val height = 103 // 7
    private val hh = (height-1) / 2
    private val seconds = 100L

    override fun part1(): Int {
        val destinatons = lines.map {line ->
            val (px, py, vx, vy) = start_position.find(line)!!.destructured
            println("$px, $py, $vx, $vy")
            val ex = (px.toLong() + seconds * vx.toLong()).mod(width)
            val ey = (py.toLong() + seconds * vy.toLong()).mod(height)
            ex to ey
        }
        val q1 = destinatons.filter { (x, y) -> x < hw && y < hh }.count()
        val q2 = destinatons.filter { (x, y) -> x < hw && y > hh }.count()
        val q3 = destinatons.filter { (x, y) -> x > hw && y < hh }.count()
        val q4 = destinatons.filter { (x, y) -> x > hw && y > hh }.count()
        println(destinatons)
        println("$q1, $q2, $q3, $q4")
        return q1*q2*q3*q4
    }

    private fun bonkers(foo: List<Pair<Pair<Int, Int>, Pair<Int, Int>>>, seconds: Int): Int {
        val destinations = foo.map { (p, v) ->
            val (px, py) = p
            val (vx, vy) = v
            val ex = (px + seconds.mod(width) * vx).mod(width)
            val ey = (py + seconds.mod(height) * vy).mod(height)
            ex to ey
        }
        return destinations.combinationsOfTwo().map { (f, s) ->
            val (fx, fy) = f
            val (sx, sy) = s
            val dx = abs(fx - sx)
            val dy = abs(fy - sy)
            dx to dy
        }.filter { (dx, dy) -> dx < 1 || dy < 1 }.count()
    }

    private fun printlnTree(foo: List<Pair<Pair<Int, Int>, Pair<Int, Int>>>, seconds: Int) {
        val destinations = foo.map { (p, v) ->
            val (px, py) = p
            val (vx, vy) = v
            val ex = (px + seconds.mod(width) * vx).mod(width)
            val ey = (py + seconds.mod(height) * vy).mod(height)
            ex to ey
        }.toSet()
        for (y in 0 until height) {
            for (x in 0 until width) {
                if (destinations.contains(x to y))
                    print('#')
                else
                    print('.')
            }
            println()
        }
        println("-------")
    }

    override fun part2(): Int {
        val foo = lines.map {line ->
            val (px, py, vx, vy) = start_position.find(line)!!.destructured
            (px.toInt() to py.toInt()) to (vx.toInt() to vy.toInt())
        }
        var last = 0
        for (s in 230 until 10000 step 101) {
            val c = bonkers(foo, s)
            if (c > 5000) {
                printlnTree(foo, s)
                println("$s $c ${s - last}")
                last = s
                return s
            }
        }
        return -1
    }
}
