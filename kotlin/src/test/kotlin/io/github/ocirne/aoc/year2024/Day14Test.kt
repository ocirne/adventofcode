package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day14Test: AocTest(Day14::class, loadExample = false) {

    @Test
    fun `examples year 2024 day 14 part 1`() {
        val day14 = Day14(loadExample(2024, "14"), width=11, height=7)
        day14.part1() shouldBe 12
    }
}
