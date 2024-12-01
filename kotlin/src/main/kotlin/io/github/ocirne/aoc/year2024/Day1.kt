package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.abs

class Day1(val lines: List<String>) : AocChallenge(2024, 1) {

    val regex = Regex("\\s+")

    override fun part1(): Int {
//        println(lines)
        val firstList = lines.map { line -> line.split(' ').get(0).toInt() }.sorted()
        val secondList = lines.map { line -> line.split(regex).get(1).toInt() }.sorted()
//        println(firstList)
//        println(secondList)
        return firstList.zip(secondList).sumOf { (f, s) -> abs(f - s) }
    }

    override fun part2(): Int {
        val firstList = lines.map { line -> line.split(' ').get(0).toInt() }
        val secondList = lines.map { line -> line.split(regex).get(1).toInt() }.groupingBy { it }.eachCount()
        println(firstList)
        println(secondList)
        return firstList.sumOf { f -> f * secondList.getOrDefault(f, 0) }
    }
}
