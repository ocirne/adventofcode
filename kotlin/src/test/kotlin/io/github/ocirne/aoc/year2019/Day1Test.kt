package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day1Test : AocTest(Day1::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 1 part 1`() {
        subject as Day1
        subject.getFuel(12) shouldBe 2
        subject.getFuel(14) shouldBe 2
        subject.getFuel(1969) shouldBe 654
        subject.getFuel(100756) shouldBe 33583
    }
}
