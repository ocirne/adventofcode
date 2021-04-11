package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day10Test {

    @Test
    fun `examples year 2015 day 10 step`() {
        Day10(listOf()).step("1".toList()) shouldBe "11".toList()
        Day10(listOf()).step("11".toList()) shouldBe "21".toList()
        Day10(listOf()).step("21".toList()) shouldBe "1211".toList()
        Day10(listOf()).step("1211".toList()) shouldBe "111221".toList()
        Day10(listOf()).step("111221".toList()) shouldBe "312211".toList()
    }
}
