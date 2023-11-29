package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day6Test : AocTest(Day6::class, 42) {

    @Test
    fun `examples year 2019 day 6 part 1`() {
        subject as Day6
        subject.countOrbits("D") shouldBe 3
        subject.countOrbits("L") shouldBe 7
        subject.countOrbits("COM") shouldBe 0
    }

    // TODO support multiple tests
    @Test
    fun `examples year 2019 day 6 part 2`() {
        subject as Day6
        subject.commonParent("K", "I") shouldBe "D"
        subject.countOrbits("K") shouldBe 6
        subject.countOrbits("I") shouldBe 4
        subject.countOrbits("D") shouldBe 3
//        subject.part2() shouldBe 2
    }
}
