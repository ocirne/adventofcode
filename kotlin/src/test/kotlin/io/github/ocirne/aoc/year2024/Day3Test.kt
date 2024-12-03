package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day3Test: AocTest(Day3::class, loadExample = false) {

    @Test
    fun `examples year 2024 day 3 part 1`() {
        val day3 = Day3(loadExample(2024, "3a"))
        day3.part1() shouldBe 161
    }

    @Test
    fun `examples year 2024 day 3 part 2`() {
        val day3 = Day3(loadExample(2024, "3b"))
        day3.part2() shouldBe 48
    }
}
