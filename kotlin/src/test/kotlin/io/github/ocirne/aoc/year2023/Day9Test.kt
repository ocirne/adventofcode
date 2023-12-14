package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day9Test: AocTest(Day9::class, 114, 2) {

    @Test
    fun `examples year 2023 day 9 part 1`() {
        subject as Day9
        subject.adjacentValue("0 3 6 9 12 15", subject::nextValue) shouldBe 18
        subject.adjacentValue("1 3 6 10 15 21", subject::nextValue) shouldBe 28
        subject.adjacentValue("10 13 16 21 30 45", subject::nextValue) shouldBe 68
    }

    @Test
    fun `examples year 2023 day 9 part 2`() {
        subject as Day9
        subject.adjacentValue("0 3 6 9 12 15", subject::previousValue) shouldBe -3
        subject.adjacentValue("1 3 6 10 15 21", subject::previousValue) shouldBe 0
        subject.adjacentValue("10 13 16 21 30 45", subject::previousValue) shouldBe 5
    }
}

