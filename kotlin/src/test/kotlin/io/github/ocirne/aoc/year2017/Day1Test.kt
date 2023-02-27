package io.github.ocirne.aoc.year2017

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day1Test : AocTest(Day1::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 1 part 1`() {
        subject as Day1
        subject.solveCaptcha1("1122") shouldBe 3
        subject.solveCaptcha1("1111") shouldBe 4
        subject.solveCaptcha1("1234") shouldBe 0
        subject.solveCaptcha1("91212129") shouldBe 9
    }

    @Test
    fun `examples year 2015 day 1 part 2`() {
        subject as Day1
        subject.solveCaptcha2("1212") shouldBe 6
        subject.solveCaptcha2("1221") shouldBe 0
        subject.solveCaptcha2("123425") shouldBe 4
        subject.solveCaptcha2("123123") shouldBe 12
        subject.solveCaptcha2("12131415") shouldBe 4
    }
}
