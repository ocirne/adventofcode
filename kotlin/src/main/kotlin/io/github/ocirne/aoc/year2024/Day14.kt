package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

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

    override fun part2(): Long {
        return -1
    }
}
