package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day17Test : AocTest(Day17::class, loadExample = false) {

    private fun foo(): Map<Pair<Long, Long>, Char> {
        val lines = loadExample(2019, "17")
        val result = mutableMapOf<Pair<Long, Long>, Char>()
        lines.forEachIndexed { y, line ->
            line.forEachIndexed { x, c ->
                if (c == '#') {
                    result[x.toLong() to y.toLong()] = c
                }
            }
        }
        return result
    }

    @Test
    fun `examples year 2019 day 17 part 1`() {
        subject as Day17
        subject.foo(foo()) shouldBe 76
    }

    @Test
    fun `examples year 2019 day 17 part 2`() {
    }
}
