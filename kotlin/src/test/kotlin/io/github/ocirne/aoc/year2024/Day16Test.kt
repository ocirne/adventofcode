package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day16Test: AocTest(Day16::class, expectedPart1 = 11048, expectedPart2 = 64) {

    @Test
    fun `examples year 2024 day 16 part 1 (smaller example)`() {
        val day16 = Day16(loadExample(2024, "16b"))
        day16.part1() shouldBe 7036
    }

    @Test
    fun `examples year 2024 day 16 part 2 (smaller example)`() {
        val day16 = Day16(loadExample(2024, "16b"))
        day16.part2() shouldBe 45
    }
}
