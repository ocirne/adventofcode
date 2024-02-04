package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day18Test : AocTest(Day18::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 18 part 1`() {
        Day18(loadExample(2019, "18a")).part1() shouldBe 8
        Day18(loadExample(2019, "18b")).part1() shouldBe 86
        Day18(loadExample(2019, "18c")).part1() shouldBe 132
        Day18(loadExample(2019, "18d")).part1() shouldBe 136
        Day18(loadExample(2019, "18e")).part1() shouldBe 81
    }

    @Test
    fun `examples year 2019 day 18 part 2`() {
        Day18(loadExample(2019, "18f")).part2() shouldBe 8
        Day18(loadExample(2019, "18g")).part2() shouldBe 24
        Day18(loadExample(2019, "18h")).part2() shouldBe 32
        Day18(loadExample(2019, "18i")).part2() shouldBe 72
    }
}
