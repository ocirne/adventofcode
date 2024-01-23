package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day20Test : AocTest(Day20::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 20 part 1`() {
        Day20(loadExample(2019, "20a", trim = false)).part1() shouldBe 23
        Day20(loadExample(2019, "20b", trim = false)).part1() shouldBe 58
    }
}
