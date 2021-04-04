package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day5Test {

    @Test
    fun `examples year 2015 day 5 part 1`() {
        day5().isNicePart1("ugknbfddgicrmopn") shouldBe true
        day5().isNicePart1("aaa") shouldBe true
        day5().isNicePart1("jchzalrnumimnmhp") shouldBe false
        day5().isNicePart1("haegwjzuvuyypxyu") shouldBe false
        day5().isNicePart1("dvszwmarrgswjxmb") shouldBe false
    }

    @Test
    fun `examples year 2015 day 5 part 2`() {
        day5().isNicePart2("qjhvhtzxzqqjkmpb") shouldBe true
        day5().isNicePart2("xxyxx") shouldBe true
        day5().isNicePart2("aaa") shouldBe false
        day5().isNicePart2("uurcxstgmygtbstg") shouldBe false
        day5().isNicePart2("ieodomkazucvgmuy") shouldBe false
    }

    private fun day5(): Day5 {
        return Day5(listOf(""))
    }
}
