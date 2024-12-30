package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.permutations

class Day21(val lines: List<String>) : AocChallenge(2024, 21) {

    val positionsNumericKeypad = mapOf(
        '1' to Pair(0, 2),
        '2' to Pair(1, 2),
        '3' to Pair(2, 2),
        '4' to Pair(0, 1),
        '5' to Pair(1, 1),
        '6' to Pair(2, 1),
        '7' to Pair(0, 0),
        '8' to Pair(1, 0),
        '9' to Pair(2, 0),
        '0' to Pair(1, 3),
        'A' to Pair(2, 3),
    )

    val positionsDirectionalKeypad = mapOf(
        '^' to Pair(1, 0),
        'A' to Pair(2, 0),
        '<' to Pair(0, 1),
        'v' to Pair(1, 1),
        '>' to Pair(2, 1),
    )

    /** Konkrete Angebote, um von src nach tgt zu kommen */
    fun numericKeyboard(srcChar: Char, tgtChar: Char): Iterable<List<Char>> {
        val pSrc = positionsNumericKeypad[srcChar]!!
        val pTgt = positionsNumericKeypad[tgtChar]!!
        val dx = pTgt.first - pSrc.first
        val dy = pTgt.second - pSrc.second
        val moves = mutableListOf<Char>()
        if (dx < 0) {
            repeat(-dx) { moves.add('<') }
        } else if (dx > 0) {
            repeat(dx) { moves.add('>') }
        }
        if (dy < 0) {
            repeat(-dy) { moves.add('^') }
        } else if (dy > 0) {
            repeat(dy) { moves.add('v') }
        }
        println("moves $moves")
        return moves.permutations()
    }

    /** Anzahl der Moves, um von src nach tgt zu kommen */
    fun directionalKeyboard(srcChar: Char, tgtChar: Char): Iterable<List<Char>> {
        val pSrc = positionsDirectionalKeypad[srcChar]!!
        val pTgt = positionsDirectionalKeypad[tgtChar]!!
        val dx = pTgt.first - pSrc.first
        val dy = pTgt.second - pSrc.second
        val moves = mutableListOf<Char>()
        if (dx < 0) {
            repeat(-dx) { moves.add('<') }
        } else if (dx > 0) {
            repeat(dx) { moves.add('>') }
        }
        if (dy < 0) {
            repeat(-dy) { moves.add('^') }
        } else if (dy > 0) {
            repeat(dy) { moves.add('v') }
        }
        return moves.permutations().toSet()
    }

    fun countMovesDirectional(foo: List<Char>): List<Char> {
        val result = mutableListOf<Char>()
        for ((s, t) in foo.zipWithNext()) {
            result.addAll(directionalKeyboard(s, t).first())
            result.add('A')
        }
        return result
    }

    fun countMovesNumeric(foo: List<Char>): List<Char> {
        val result = mutableListOf<Char>()
        for ((s, t) in foo.zipWithNext()) {
            var bestSize = 10000
            var bestAngebot = listOf<Char>()
            var bestNextLevel = listOf<Char>()
            for (angebot in numericKeyboard(s, t)) {
                val nextLevel = countMovesDirectional(listOf('A') + angebot)
                println("($s -> $t) angebot $angebot nL $nextLevel")
                if (bestSize > nextLevel.size) {
                    bestSize = nextLevel.size
                    bestAngebot = angebot
                    bestNextLevel = nextLevel
                }
            }
            println("----- $bestAngebot - $bestNextLevel ----")
            result.addAll(bestAngebot)
            result.add('A')
        }
        return result
    }

    fun foo(s: List<Char>): Int {
        val result = countMovesNumeric(listOf('A') + s)
        println(result.joinToString(""))
        return result.size
    }

    override fun part1(): Int {
        var total = 0
        for (line in listOf("029A")) {
            val length = foo(line.toList())
            val value = line.dropLast(1).toInt()
            println("$line $length $value")
            total += length * value
        }
        return total
    }

    override fun part2(): Int {
        return -1
    }
}
