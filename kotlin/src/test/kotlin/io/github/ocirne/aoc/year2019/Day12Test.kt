package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day12Test : AocTest(Day12::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 12 part 1`() {
        Day12(loadExample(2019, "12a")).foo(steps=10) shouldBe 179
        Day12(loadExample(2019, "12b")).foo(steps=100) shouldBe 1940
    }

    @Test
    fun `examples year 2019 day 12 part 2`() {
    }
}
