package io.github.ocirne.aoc.year2017

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day1Test {

    @Test
    fun `examples year 2015 day 1 part 1`() {
        Day1(listOf("1122")).part1() shouldBe 3
        Day1(listOf("1111")).part1() shouldBe 4
        Day1(listOf("1234")).part1() shouldBe 0
        Day1(listOf("91212129")).part1() shouldBe 9
    }

    @Test
    fun `examples year 2015 day 1 part 2`() {
        Day1(listOf("1212")).part2() shouldBe 6
        Day1(listOf("1221")).part2() shouldBe 0
        Day1(listOf("123425")).part2() shouldBe 4
        Day1(listOf("123123")).part2() shouldBe 12
        Day1(listOf("12131415")).part2() shouldBe 4
    }
}
