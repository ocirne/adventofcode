package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day01Test {

    @Test
    fun `examples 2015 day 01 part1`() {
        Day01(listOf("(())")).part1() shouldBe 0
        Day01(listOf("()()")).part1() shouldBe 0
        Day01(listOf("(((")).part1() shouldBe 3
        Day01(listOf("(()(()(")).part1() shouldBe 3
        Day01(listOf("))(((((")).part1() shouldBe 3
        Day01(listOf("())")).part1() shouldBe -1
        Day01(listOf("))(")).part1() shouldBe -1
        Day01(listOf(")))")).part1() shouldBe -3
        Day01(listOf(")())())")).part1() shouldBe -3
    }

    @Test
    fun `examples 2015 day 01 part2`() {
        Day01(listOf(")")).part2() shouldBe 1
        Day01(listOf("()())")).part2() shouldBe 5
    }
}
