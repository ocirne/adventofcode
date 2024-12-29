package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.maps.shouldNotContainKey
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day22Test: AocTest(Day22::class, expectedPart1 = 37327623) {

    @Test
    fun `examples year 2024 day 22 part 2`() {
        val subject = Day22(loadExample(2024, "22b"))
        subject.part2() shouldBe 23
    }

    @Test
    fun `examples year 2024 day 22 part 2 bar`() {
        subject as Day22
        val key = "-2,1,-1,3"
        subject.bar(1).toMap()[key] shouldBe 7
        subject.bar(2).toMap()[key] shouldBe 7
        subject.bar(3).toMap() shouldNotContainKey key
        subject.bar(2024).toMap()[key] shouldBe 9
    }
}
