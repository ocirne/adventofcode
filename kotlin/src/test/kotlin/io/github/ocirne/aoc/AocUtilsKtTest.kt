package io.github.ocirne.aoc

import io.kotest.matchers.collections.shouldContainAll
import org.junit.jupiter.api.Test

class AocUtilsKtTest {

    @Test
    fun `can permutate a set of Integers`() {
        val numbers = setOf(1, 2, 3)
        val actual = numbers.permutations()
        actual shouldContainAll listOf(
            listOf(1, 2, 3),
            listOf(1, 3, 2),
            listOf(2, 1, 3),
            listOf(2, 3, 1),
            listOf(3, 1, 2),
            listOf(3, 2, 1)
        )
    }

    @Test
    fun `can permutate a list of Integers`() {
        val numbers = listOf(1, 2, 3)
        val actual = numbers.permutations()
        actual shouldContainAll listOf(
            listOf(1, 2, 3),
            listOf(1, 3, 2),
            listOf(2, 1, 3),
            listOf(2, 3, 1),
            listOf(3, 1, 2),
            listOf(3, 2, 1)
        )
    }

    @Test
    fun `can permutate a list of Integers with duplicates`() {
        val numbers = listOf(1, 2, 2)
        val actual = numbers.permutations()
        actual.toSet() shouldContainAll listOf(
            listOf(1, 2, 2),
            listOf(2, 1, 2),
            listOf(2, 2, 1)
        )
    }
}
