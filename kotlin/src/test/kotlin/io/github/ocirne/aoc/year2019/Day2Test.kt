package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day2Test : AocTest(Day2::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 2 part 1`() {
        IntCodeEmulator2019("1,0,0,0,99").run().toString() shouldBe "2,0,0,0,99"
        IntCodeEmulator2019("2,3,0,3,99").run().toString() shouldBe "2,3,0,6,99"
        IntCodeEmulator2019("2,4,4,5,99,0").run().toString() shouldBe "2,4,4,5,99,9801"
        IntCodeEmulator2019("1,1,1,4,99,5,6,0,99").run().toString() shouldBe "30,1,1,4,2,5,6,0,99"
        IntCodeEmulator2019("1,9,10,3,2,3,11,0,99,30,40,50").run()
            .toString() shouldBe "3500,9,10,70,2,3,11,0,99,30,40,50"
    }
}
