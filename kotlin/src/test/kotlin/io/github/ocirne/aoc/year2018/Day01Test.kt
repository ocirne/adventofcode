package io.github.ocirne.aoc.year2018

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day01Test {

    @Test
    fun `examples year 2018 day 1 part 1`() {
        Day01("+1, +1, +1".split(", ")).part1() shouldBe 3
        Day01("+1, +1, -2".split(", ")).part1() shouldBe 0
        Day01("-1, -2, -3".split(", ")).part1() shouldBe -6
    }
}