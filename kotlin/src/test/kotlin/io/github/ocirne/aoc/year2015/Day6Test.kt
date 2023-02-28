package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day6Test : AocTest(Day6::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 6 part 1`() {
        Day6(
            listOf(
                "turn on 0,0 through 999,999",
                "toggle 0,0 through 999,0",
                "turn off 499,499 through 500,500"
            )
        ).part1() shouldBe 1000000 - 1000 - 4
    }

    @Test
    fun `examples year 2015 day 6 part 2`() {
        Day6(
            listOf(
                "turn on 0,0 through 0,0",
                "toggle 0,0 through 999,999"
            )
        ).part2() shouldBe 1 + 2000000
    }
}
