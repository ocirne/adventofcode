package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocTest
import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

internal class Day8Test : AocTest(Day8::class, loadExample = false) {

    @Test
    fun `examples year 2015 day 8 shrink (part 1)`() {
        subject as Day8
        subject.shrink("""  ""  """.trim()) shouldBe 2
        subject.shrink("""  "abc"  """.trim()) shouldBe 2
        subject.shrink("""  "aaa\"aaa"  """.trim()) shouldBe 3
        subject.shrink("""  "\x27"  """.trim()) shouldBe 5
    }

    @Test
    fun `examples year 2015 day 8 expand (part 2)`() {
        subject as Day8
        subject.expand("""  ""  """.trim()) shouldBe 4
        subject.expand("""  "abc"  """.trim()) shouldBe 4
        subject.expand("""  "aaa\"aaa"  """.trim()) shouldBe 6
        subject.expand("""  "\x27"  """.trim()) shouldBe 5
    }
}
