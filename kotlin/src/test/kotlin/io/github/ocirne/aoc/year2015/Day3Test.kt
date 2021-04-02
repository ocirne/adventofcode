package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day3Test {

    @Test
    fun `examples year 2015 day 3 part 1`() {
        Day3(listOf(">")).part1() shouldBe 2
        Day3(listOf("^>v<")).part1() shouldBe 4
        Day3(listOf("^v^v^v^v^v")).part1() shouldBe 2
    }

    @Test
    fun `examples year 2015 day 3 part 2`() {
        Day3(listOf("^v")).part2() shouldBe  3
        Day3(listOf("^>v<")).part2() shouldBe  3
        Day3(listOf("^v^v^v^v^v")).part2() shouldBe 11
    }
}
