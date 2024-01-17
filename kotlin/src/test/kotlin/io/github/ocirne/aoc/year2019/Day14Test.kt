package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day14Test : AocTest(Day14::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 14 part 1`() {
        Day14(loadExample(2019, "14a")).part1() shouldBe 31L
        Day14(loadExample(2019, "14b")).part1() shouldBe 165L
        Day14(loadExample(2019, "14c")).part1() shouldBe 13312L
        Day14(loadExample(2019, "14d")).part1() shouldBe 180697L
        Day14(loadExample(2019, "14e")).part1() shouldBe 2210736L
    }

    @Test
    fun `examples year 2019 day 14 part 2`() {
        Day14(loadExample(2019, "14c")).part2() shouldBe 82892753L
        Day14(loadExample(2019, "14d")).part2() shouldBe 5586022L
        Day14(loadExample(2019, "14e")).part2() shouldBe 460664L
    }
}
