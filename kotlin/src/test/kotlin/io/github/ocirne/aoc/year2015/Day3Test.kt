package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day3Test: AocTest(Day3::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 3 part 1`() {
        subject as Day3
        subject.solve1(">") shouldBe 2
        subject.solve1("^>v<") shouldBe 4
        subject.solve1("^v^v^v^v^v") shouldBe 2
    }

    @Test
    fun `examples year 2015 day 3 part 2`() {
        subject as Day3
        subject.solve2("^v") shouldBe  3
        subject.solve2("^>v<") shouldBe  3
        subject.solve2("^v^v^v^v^v") shouldBe 11
    }
}
