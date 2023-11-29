package io.github.ocirne.aoc

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Assumptions
import org.junit.jupiter.api.Test
import kotlin.reflect.KClass

abstract class AocTest(
    aocChallengeClass: KClass<out AocChallenge>,
    private val expectedPart1: Any? = null,
    private val expectedPart2: Any? = null,
    loadExample: Boolean = true
) {

    val subject = createAocChallenge(aocChallengeClass, loadExample)

    @Test
    fun `examples part 1 is correct`() {
        Assumptions.assumeTrue(expectedPart1 != null)
        subject.part1() shouldBe expectedPart1
    }

    @Test
    fun `examples part 2 is correct`() {
        Assumptions.assumeTrue(expectedPart2 != null)
        subject.part2() shouldBe expectedPart2
    }

    companion object {

        fun createAocChallenge(dayClass: KClass<out AocChallenge>, loadExample: Boolean): AocChallenge {
            val peek = dayClass.constructors.first().call(listOf<String>())
            if (!loadExample) {
                return peek
            }
            val content = this::class.java.classLoader
                .getResourceAsStream("examples/${peek.year}/${peek.day}.txt")!!
                .bufferedReader()
                .readLines()
                .map { it.trim() }
            return dayClass.constructors.first().call(content)
        }
    }
}
