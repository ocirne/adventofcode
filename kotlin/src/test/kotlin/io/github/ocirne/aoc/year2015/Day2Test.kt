package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day2Test: AocTest(Day2::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 2 part 1`() {
        Day2(listOf("2x3x4")).part1() shouldBe 58
        Day2(listOf("1x1x10")).part1() shouldBe 43
    }

    @Test
    fun `examples year 2015 day 2 part 2`() {
        Day2(listOf("2x3x4")).part2() shouldBe 34
        Day2(listOf("1x1x10")).part2() shouldBe 14
    }
}
