package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day4Test {

    @Test
    fun `examples year 2015 day 4 part 1`() {
        Day4(listOf("abcdef")).search(5) shouldBe 609043
        Day4(listOf("pqrstuv")).search(5) shouldBe 1048970
    }
}
