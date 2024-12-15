package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day15Test: AocTest(Day15::class, expectedPart1 = 2028) {

    @Test
    fun `examples year 2024 day 15 part 1 (larger example)`() {
        val day15 = Day15(loadExample(2024, "15_large"))
        day15.part1() shouldBe 10092
    }
}
