package io.github.ocirne.aoc.year2022

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day3Test {

    @Test
    fun `examples year 2022 day 3 part 1`() {
        Day3(lines).part1() shouldBe 157
    }

    @Test
    fun `examples year 2022 day 3 part 2`() {
        Day3(lines).part2() shouldBe 70
    }

    companion object {
        val lines = this::class.java.classLoader
            .getResourceAsStream("examples/2022/3.txt")!!
            .bufferedReader()
            .readLines()
            .map { it.trim() }
    }
}