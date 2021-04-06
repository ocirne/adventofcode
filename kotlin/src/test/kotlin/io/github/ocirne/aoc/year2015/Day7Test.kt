package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day7Test {

    @Test
    fun `examples year 2015 day 7`() {
        Day7(lines).run("d") shouldBe 72
        Day7(lines).run("e") shouldBe 507
        Day7(lines).run("f") shouldBe 492
        Day7(lines).run("g") shouldBe 114
        Day7(lines).run("h") shouldBe 65412
        Day7(lines).run("i") shouldBe 65079
        Day7(lines).run("x") shouldBe 123
        Day7(lines).run("y") shouldBe 456
    }

    companion object {
        val lines = this::class.java.classLoader
            .getResourceAsStream("examples/2015/7.txt")!!
            .bufferedReader()
            .readLines()
    }
}
