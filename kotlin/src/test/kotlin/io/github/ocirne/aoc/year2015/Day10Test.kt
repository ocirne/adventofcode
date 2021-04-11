package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day10Test {

    @Test
    fun `examples year 2015 day 10 step`() {
        Day10(listOf()).step("1") shouldBe "11"
        Day10(listOf()).step("11") shouldBe "21"
        Day10(listOf()).step("21") shouldBe "1211"
        Day10(listOf()).step("1211") shouldBe "111221"
        Day10(listOf()).step("111221") shouldBe "312211"
    }
}
