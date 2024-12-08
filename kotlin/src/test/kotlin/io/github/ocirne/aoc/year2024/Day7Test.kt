package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day7Test: AocTest(Day7::class, expectedPart1 = 3749L) {

    @Test
    fun `examples year 2024 day 7 part 2`() {
        val day7 = Day7(loadExample(2024, "7b"))
        day7.part2() shouldBe 19025L
    }
}
