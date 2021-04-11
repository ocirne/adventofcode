package io.github.ocirne.aoc.year2015

import io.kotest.matchers.collections.shouldContainAll
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day9Test {

    @Test
    fun `can generate permutations`() {
        val numbers = setOf(1, 2, 3)
        val permutations = numbers.permutations()
        System.err.println(permutations)
        permutations shouldContainAll listOf(
            listOf(1,2,3),
            listOf(1,3,2),
            listOf(2,1,3),
            listOf(2,3,1),
            listOf(3,1,2),
            listOf(3,2,1));
    }

    @Test
    fun `examples year 2015 day 9 part 1`() {
        Day9(lines).part1() shouldBe 605
        Day9(lines).part2() shouldBe 982
    }

    companion object {
        val lines = this::class.java.classLoader
            .getResourceAsStream("examples/2015/9.txt")!!
            .bufferedReader()
            .readLines()
    }
}
