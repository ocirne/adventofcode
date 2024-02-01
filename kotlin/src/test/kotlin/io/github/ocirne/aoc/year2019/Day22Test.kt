package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day22Test : AocTest(Day22::class, loadExample = false) {

    private class NaiveShuffler: Day22.Shuffler<List<Int>>() {

        override fun dealIntoNewStack(acc: List<Int>): List<Int> {
            return acc.reversed()
        }

        override fun cutN(acc: List<Int>, n: Int): List<Int> {
            assert(n != 0)
            return if (n > 0) {
                acc.drop(n) + acc.take(n)
            } else {
                acc.drop(acc.size + n) + acc.take(acc.size + n)
            }
        }

        override fun dealWithIncrementP(acc: List<Int>, n: Int): List<Int> {
            val nextDeck = acc.toList().toMutableList()
            acc.indices.forEach { i ->
                nextDeck[(i * n) % acc.size] = acc[i]
            }
            return nextDeck
        }
    }

    private fun naiveOneLine(shuffle: String, deck: IntRange): List<Int> {
        return NaiveShuffler().applyOneLine(shuffle, deck.toList())
    }

    private fun naiveShuffler(lines: List<String>, deck: IntRange): List<Int> {
        return NaiveShuffler().shuffle(lines, deck.toList())
    }

    @Test
    fun `can deal into new stack`() {
        naiveOneLine("deal into new stack", 0..9) shouldBe
                listOf(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    }

    @Test
    fun `can cut 3`() {
        naiveOneLine("cut 3", 0..9) shouldBe
                listOf(3, 4, 5, 6, 7, 8, 9, 0, 1, 2)
    }

    @Test
    fun `can cut -4`() {
        naiveOneLine("cut -4", 0..9) shouldBe
                listOf(6, 7, 8, 9, 0, 1, 2, 3, 4, 5)
    }

    @Test
    fun `can deal with increment p`() {
        naiveOneLine("deal with increment 3", 0..9) shouldBe
                listOf(0, 7, 4, 1, 8, 5, 2, 9, 6, 3)
    }

    @Test
    fun `examples year 2019 day 22 part 1`() {
        naiveShuffler(loadExample(2019, "22a"), 0..9) shouldBe listOf(0, 3, 6, 9, 2, 5, 8, 1, 4, 7)
        naiveShuffler(loadExample(2019, "22b"), 0..9) shouldBe listOf(3, 0, 7, 4, 1, 8, 5, 2, 9, 6)
        naiveShuffler(loadExample(2019, "22c"), 0..9) shouldBe listOf(6, 3, 0, 7, 4, 1, 8, 5, 2, 9)
        naiveShuffler(loadExample(2019, "22d"), 0..9) shouldBe listOf(9, 2, 5, 8, 1, 4, 7, 0, 3, 6)
    }
}
