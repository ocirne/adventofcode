package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day9Test : AocTest(Day9::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 9 part 1`() {
        val quine = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
        IntCodeEmulator2019(quine).run().getOutput() shouldBe quine
        IntCodeEmulator2019("1102,34915192,34915192,7,4,7,99,0").run().getLastOutput() shouldBe 1219070632396864L
        IntCodeEmulator2019("104,1125899906842624,99").run().getLastOutput() shouldBe 1125899906842624L
    }
}