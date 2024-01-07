package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day10Test : AocTest(Day10::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 10 part 1`() {
        Day10(loadExample(2019, "10a")).part1() shouldBe 8
        Day10(loadExample(2019, "10b")).part1() shouldBe 33
        Day10(loadExample(2019, "10c")).part1() shouldBe 35
        Day10(loadExample(2019, "10d")).part1() shouldBe 41
        Day10(loadExample(2019, "10e")).part1() shouldBe 210
    }
}