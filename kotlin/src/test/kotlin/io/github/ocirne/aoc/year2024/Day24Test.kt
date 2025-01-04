package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day24Test: AocTest(Day24::class, expectedPart1 = 4) {

    @Test
    fun `examples year 2024 day 24 part 1`() {
        val subject = Day24(loadExample(2024, "24b"))
        subject.part1() shouldBe 2024
    }
}
