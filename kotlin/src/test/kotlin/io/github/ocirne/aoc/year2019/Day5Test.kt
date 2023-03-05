package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day5Test : AocTest(Day5::class, loadExample = false) {

    @Test
    fun `examples year 2019 day 5 part 1`() {
        IntCodeEmulatorDay5("3,0,4,0,99").run(listOf(42)).output.last() shouldBe 42
        IntCodeEmulatorDay5("1002,4,3,4,33").run(listOf()).toString() shouldBe "1002,4,3,4,99"
        IntCodeEmulatorDay5("1101,100,-1,4,0").run(listOf()).toString() shouldBe "1101,100,-1,4,99"
    }


    3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).

    3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
    3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)

    3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99

    The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.


}
