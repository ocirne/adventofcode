package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day1Test {

    @Test
    fun `examples year 2015 day 1 part 1`() {
        Day1(listOf("(())")).part1() shouldBe 0
        Day1(listOf("()()")).part1() shouldBe 0
        Day1(listOf("(((")).part1() shouldBe 3
        Day1(listOf("(()(()(")).part1() shouldBe 3
        Day1(listOf("))(((((")).part1() shouldBe 3
        Day1(listOf("())")).part1() shouldBe -1
        Day1(listOf("))(")).part1() shouldBe -1
        Day1(listOf(")))")).part1() shouldBe -3
        Day1(listOf(")())())")).part1() shouldBe -3
    }

    @Test
    fun `examples year 2015 day 1 part 2`() {
        Day1(listOf(")")).part2() shouldBe 1
        Day1(listOf("()())")).part2() shouldBe 5
    }
}
