package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day16Test : AocTest(Day16::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 16 part 1`() {
        subject as Day16
        subject.naive("12345678", 1) shouldBe "48226158"
        subject.naive("12345678", 2) shouldBe "34040438"
        subject.naive("12345678", 3) shouldBe "03415518"
        subject.naive("12345678", 4) shouldBe "01029498"

        subject.naive("80871224585914546619083218645595") shouldBe "24176176"
        subject.naive("19617804207202209144916044189917") shouldBe "73745418"
        subject.naive("69317163492948606335995924319873") shouldBe "52432133"
    }
}
