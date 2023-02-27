package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day4Test: AocTest(Day4::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 4 part 1`() {
        subject as Day4
        subject.search("abcdef", 5) shouldBe 609043
        subject.search("pqrstuv", 5) shouldBe 1048970
    }
}
