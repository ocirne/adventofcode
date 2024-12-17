package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day17Test: AocTest(Day17::class, expectedPart1 = "4,6,3,5,6,3,5,2,1,0") {

    @Test
    fun `examples year 2024 day 17 part 2 (smaller example)`() {
        val day17 = Day17(loadExample(2024, "17b"))
        day17.part2() shouldBe 117440
    }
}
