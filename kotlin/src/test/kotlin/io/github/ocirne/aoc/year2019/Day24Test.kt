package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day24Test : AocTest(Day24::class, expectedPart1 = 2129920) {

    @Test
    fun `examples year 2019 day 24 part 2`() {
        subject as Day24
        subject.simulate(10) shouldBe 99
    }
}
