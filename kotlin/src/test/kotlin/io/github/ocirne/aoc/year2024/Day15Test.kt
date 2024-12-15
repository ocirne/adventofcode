package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day15Test: AocTest(Day15::class, expectedPart1 = 10092, expectedPart2 = 9021) {

    @Test
    fun `examples year 2024 day 15 part 1 (smaller example)`() {
        val day15 = Day15(loadExample(2024, "15_small_a"))
        day15.part1() shouldBe 2028
    }

    @Test
    fun `examples year 2024 day 15 part 2 (smaller example)`() {
        val day15 = Day15(loadExample(2024, "15_small_b"))
        day15.part2() shouldBe 618
    }
}
