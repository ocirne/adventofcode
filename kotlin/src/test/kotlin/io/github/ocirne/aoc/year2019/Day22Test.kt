package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day22Test : AocTest(Day22::class, loadExample = false) {

    @Test
    fun `can deal into new stack`() {
        subject as Day22
        subject.bar("deal into new stack", 0..9) shouldBe
                listOf(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    }

    @Test
    fun `can cut 3`() {
        subject as Day22
        subject.bar("cut 3", 0..9) shouldBe
                listOf(3, 4, 5, 6, 7, 8, 9, 0, 1, 2)
    }

    @Test
    fun `can cut -4`() {
        subject as Day22
        subject.bar("cut -4", 0..9) shouldBe
                listOf(6, 7, 8, 9, 0, 1, 2, 3, 4, 5)
    }

    @Test
    fun `can deal with increment p`() {
        subject as Day22
        subject.bar("deal with increment 3", 0..9) shouldBe
                listOf(0, 7, 4, 1, 8, 5, 2, 9, 6, 3)
    }

    @Test
    fun `examples year 2019 day 22 part 1`() {
        Day22(loadExample(2019, "22a")).foo(0..9) shouldBe listOf(0, 3, 6, 9, 2, 5, 8, 1, 4, 7)
        Day22(loadExample(2019, "22b")).foo(0..9) shouldBe listOf(3, 0, 7, 4, 1, 8, 5, 2, 9, 6)
        Day22(loadExample(2019, "22c")).foo(0..9) shouldBe listOf(6, 3, 0, 7, 4, 1, 8, 5, 2, 9)
        Day22(loadExample(2019, "22d")).foo(0..9) shouldBe listOf(9, 2, 5, 8, 1, 4, 7, 0, 3, 6)
    }

    @Test
    fun `examples year 2019 day 22 part 2`() {
    }
}
