package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day15Test: AocTest(Day15::class, 1320, 145) {

    @Test
    fun `examples year 2023 day 15 part 1`() {
        subject as Day15
       subject.aocHash("rn=1") shouldBe 30
        subject.aocHash("cm-") shouldBe 253
        subject.aocHash("qp=3") shouldBe 97
        subject.aocHash("cm=2") shouldBe 47
        subject.aocHash("qp-") shouldBe 14
        subject.aocHash("pc=4") shouldBe 180
        subject.aocHash("ot=9") shouldBe 9
        subject.aocHash("ab=5") shouldBe 197
        subject.aocHash("pc-") shouldBe 48
        subject.aocHash("pc=6") shouldBe 214
        subject.aocHash("ot=7") shouldBe 231
    }
}
