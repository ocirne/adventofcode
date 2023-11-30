package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day8Test : AocTest(Day8::class) {

    @Test
    fun `examples year 2019 day 8 part 1`() {
        subject as Day8
        subject.checkUncorrupted(width = 3, height = 2) shouldBe 1
    }

    @Test
    fun `examples year 2019 day 8 part 2`() {
        subject as Day8
    }
}
