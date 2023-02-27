package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day10Test: AocTest(Day10::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 10 step`() {
        subject as Day10
        subject.step("1".toList()) shouldBe "11".toList()
        subject.step("11".toList()) shouldBe "21".toList()
        subject.step("21".toList()) shouldBe "1211".toList()
        subject.step("1211".toList()) shouldBe "111221".toList()
        subject.step("111221".toList()) shouldBe "312211".toList()
    }
}
