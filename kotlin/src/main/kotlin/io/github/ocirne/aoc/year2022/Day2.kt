package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge

typealias ScoringFunction = (Day2.Shape, Char) -> Pair<Day2.Shape, Day2.Score>

class Day2(val lines: List<String>) : AocChallenge(2022, 2) {

    enum class Shape(val score: Int) {
        ROCK(1),
        PAPER(2),
        SCISSOR(3),
    }

    enum class Score(val score: Int) {
        WIN(6),
        DRAW(3),
        LOST(0)
    }

    // opponent, me, score
    private val result = listOf(
        Triple(Shape.ROCK, Shape.ROCK, Score.DRAW),
        Triple(Shape.ROCK, Shape.PAPER, Score.WIN),
        Triple(Shape.ROCK, Shape.SCISSOR, Score.LOST),
        Triple(Shape.PAPER, Shape.ROCK, Score.LOST),
        Triple(Shape.PAPER, Shape.PAPER, Score.DRAW),
        Triple(Shape.PAPER, Shape.SCISSOR, Score.WIN),
        Triple(Shape.SCISSOR, Shape.ROCK, Score.WIN),
        Triple(Shape.SCISSOR, Shape.PAPER, Score.LOST),
        Triple(Shape.SCISSOR, Shape.SCISSOR, Score.DRAW),
    )

    private val mappingOpponent = mapOf(
        'A' to Shape.ROCK,
        'B' to Shape.PAPER,
        'C' to Shape.SCISSOR,
    )

    private val mapping1 = mapOf(
        'X' to Shape.ROCK,
        'Y' to Shape.PAPER,
        'Z' to Shape.SCISSOR,
    )

    private val mapping2 = mapOf(
        'X' to Score.LOST,
        'Y' to Score.DRAW,
        'Z' to Score.WIN,
    )

    private val scoringPart1: ScoringFunction = { opponentShape, me ->
        val myShape: Shape = mapping1[me]!!
        val score: Score = result.first { (o, m, _) -> o == opponentShape && m == myShape }.third
        Pair(myShape, score)
    }

    private val scoringPart2: ScoringFunction = { opponentShape, me ->
        val score: Score = mapping2[me]!!
        val myShape: Shape = result.first { (o, _, s) -> o == opponentShape && s == score }.second
        Pair(myShape, score)
    }

    private fun scoreLines(scoringFun: ScoringFunction): Int {
        return lines
            .asSequence()
            .filter { line -> line.isNotBlank() }
            .map { line -> line.trim().split(' ') }
            .map { p -> Pair(p[0].first(), p[1].first())}
            .map { (opponent, me) -> scoringFun.invoke(mappingOpponent[opponent]!!, me) }
            .map { (m, s) -> m.score + s.score }
            .sum()
    }

    override fun part1(): Int {
        return scoreLines(scoringPart1)
    }

    override fun part2(): Int {
        return scoreLines(scoringPart2)
    }
}
