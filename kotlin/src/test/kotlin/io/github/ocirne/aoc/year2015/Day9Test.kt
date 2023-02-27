package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.collections.shouldContainAll
import org.junit.jupiter.api.Test

internal class Day9Test: AocTest(Day9::class, 605, 982) {

    @Test
    fun `can generate permutations`() {
        val numbers = setOf(1, 2, 3)
        val permutations = numbers.permutations()
        permutations shouldContainAll listOf(
            listOf(1,2,3),
            listOf(1,3,2),
            listOf(2,1,3),
            listOf(2,3,1),
            listOf(3,1,2),
            listOf(3,2,1));
    }
}
