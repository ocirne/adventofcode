package io.github.ocirne.aoc.year2022

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day2Test {

    private val example = """
        A Y
        B X
        C Z
    """.lines()

    @Test
    fun `examples year 2022 day 2 part 1`() {
        Day2(example).part1() shouldBe 15
    }

    @Test
    fun `examples year 2022 day 2 part 2`() {
        Day2(example).part2() shouldBe 12
    }
}