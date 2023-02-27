package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day7Test: AocTest(Day7::class) {

    @Test
    fun `examples year 2015 day 7`() {
        subject as Day7
        subject.run("d") shouldBe 72
        subject.run("e") shouldBe 507
        subject.run("f") shouldBe 492
        subject.run("g") shouldBe 114
        subject.run("h") shouldBe 65412
        subject.run("i") shouldBe 65079
        subject.run("x") shouldBe 123
        subject.run("y") shouldBe 456
    }
}
