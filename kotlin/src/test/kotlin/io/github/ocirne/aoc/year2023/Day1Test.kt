package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test

internal class Day1Test: AocTest(Day1::class, loadExample = false) {

    @Test
    fun `examples year 2023 day 1 part 1`() {
        val day1 = Day1(loadExample(2023, "1a"))
        day1.part1() shouldBe 142
    }


    @Disabled
    @Test
    fun `examples year 2023 day 1 part 2`() {
        val day1 = Day1(loadExample(2023, "1b"))
        day1.part2() shouldBe 281
    }
}
