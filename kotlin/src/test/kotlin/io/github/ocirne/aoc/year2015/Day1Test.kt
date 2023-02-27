package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day1Test : AocTest(Day1::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 1 part 1`() {
        subject as Day1
        subject.countBrackets("(())") shouldBe 0
        subject.countBrackets("()()") shouldBe 0
        subject.countBrackets("(((") shouldBe 3
        subject.countBrackets("(()(()(") shouldBe 3
        subject.countBrackets("))(((((") shouldBe 3
        subject.countBrackets("())") shouldBe -1
        subject.countBrackets("))(") shouldBe -1
        subject.countBrackets(")))") shouldBe -3
        subject.countBrackets(")())())") shouldBe -3
    }

    @Test
    fun `examples year 2015 day 1 part 2`() {
        subject as Day1
        subject.findBasement(")") shouldBe 1
        subject.findBasement("()())") shouldBe 5
    }
}
