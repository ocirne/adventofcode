package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day5Test: AocTest(Day5::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 5 part 1`() {
        subject as Day5
        subject.isNicePart1("ugknbfddgicrmopn") shouldBe true
        subject.isNicePart1("aaa") shouldBe true
        subject.isNicePart1("jchzalrnumimnmhp") shouldBe false
        subject.isNicePart1("haegwjzuvuyypxyu") shouldBe false
        subject.isNicePart1("dvszwmarrgswjxmb") shouldBe false
    }

    @Test
    fun `examples year 2015 day 5 part 2`() {
        subject as Day5
        subject.isNicePart2("qjhvhtzxzqqjkmpb") shouldBe true
        subject.isNicePart2("xxyxx") shouldBe true
        subject.isNicePart2("aaa") shouldBe false
        subject.isNicePart2("uurcxstgmygtbstg") shouldBe false
        subject.isNicePart2("ieodomkazucvgmuy") shouldBe false
    }
}
