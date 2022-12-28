package io.github.ocirne.aoc.year2022

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day1Test {

    private val example = """1000
        2000
        3000

        4000

        5000
        6000

        7000
        8000
        9000

        10000""".lines()

    @Test
    fun `examples year 2022 day 1 part 1`() {
        Day1(example).part1() shouldBe 24000
    }

    @Test
    fun `examples year 2022 day 1 part 2`() {
        Day1(example).part2() shouldBe 45000
    }
}