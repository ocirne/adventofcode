package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.github.ocirne.aoc.loadExample
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.PI

internal class Day10Test : AocTest(Day10::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 10 part 1`() {
        Day10(loadExample(2019, "10a")).part1() shouldBe 8
        Day10(loadExample(2019, "10b")).part1() shouldBe 33
        Day10(loadExample(2019, "10c")).part1() shouldBe 35
        Day10(loadExample(2019, "10d")).part1() shouldBe 41
        Day10(loadExample(2019, "10e")).part1() shouldBe 210
    }

    @Test
    fun `examples year 2019 day 10 part 2`() {
        Day10(loadExample(2019, "10e")).part2() shouldBe 802
    }

    @Test
    fun `year 2019 day 10 polar coordinates`() {
        subject as Day10
        subject.foo(Day10.Asteroid(0, 0), Day10.Asteroid(0, -1)) shouldBe (0 to 1.0)
        subject.foo(Day10.Asteroid(0, 0), Day10.Asteroid(1, 0)) shouldBe ((10000 * PI / 2).toInt() to 1.0)
        subject.foo(Day10.Asteroid(0, 0), Day10.Asteroid(0, 1)) shouldBe ((10000 * PI).toInt() to 1.0)
        subject.foo(Day10.Asteroid(0, 0), Day10.Asteroid(-1, 0)) shouldBe ((10000 * 3 * PI / 2).toInt() to 1.0)
    }
}