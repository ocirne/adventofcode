package io.github.ocirne.aoc.year2015

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day8Test {

    @Test
    fun `examples year 2015 day 8 shrink (part 1)`() {
        Day8(listOf()).shrink("""  ""  """.trim()) shouldBe 2
        Day8(listOf()).shrink("""  "abc"  """.trim()) shouldBe 2
        Day8(listOf()).shrink("""  "aaa\"aaa"  """.trim()) shouldBe 3
        Day8(listOf()).shrink("""  "\x27"  """.trim()) shouldBe 5
    }

    @Test
    fun `examples year 2015 day 8 expand (part 2)`() {
        Day8(listOf()).expand("""  ""  """.trim()) shouldBe 4
        Day8(listOf()).expand("""  "abc"  """.trim()) shouldBe 4
        Day8(listOf()).expand("""  "aaa\"aaa"  """.trim()) shouldBe 6
        Day8(listOf()).expand("""  "\x27"  """.trim()) shouldBe 5
    }
}
