package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import io.github.ocirne.aoc.permutations

private data class Position(val x: Int, val y: Int)

private typealias Keypad = Map<Char, Position>

private data class Direction(val dx: Int, val dy: Int)

class Day21(val lines: List<String>) : AocChallenge(2024, 21) {

    private val positionsNumericKeypad: Keypad = mapOf(
        '1' to Position(0, 2),
        '2' to Position(1, 2),
        '3' to Position(2, 2),
        '4' to Position(0, 1),
        '5' to Position(1, 1),
        '6' to Position(2, 1),
        '7' to Position(0, 0),
        '8' to Position(1, 0),
        '9' to Position(2, 0),
        '0' to Position(1, 3),
        'A' to Position(2, 3),
    )

    private val positionsDirectionalKeypad: Keypad = mapOf(
        '^' to Position(1, 0),
        'A' to Position(2, 0),
        '<' to Position(0, 1),
        'v' to Position(1, 1),
        '>' to Position(2, 1),
    )


    private val nswe = mapOf(
        '<' to Direction(-1, 0),
        '>' to Direction(1, 0),
        '^' to Direction(0, -1),
        'v' to Direction(0, 1),
    )

    private val A = listOf('A')

    private fun allowed(keypad: Keypad, pSrc: Position, move: List<Char>): Boolean {
        var (px, py) = pSrc
        for (m in move) {
            px += nswe[m]!!.dx
            py += nswe[m]!!.dy
            if (Position(px, py) !in keypad.values) {
                return false
            }
        }
        return true
    }

    private fun movesOnKeypad(keypad: Keypad, srcChar: Char, tgtChar: Char): Iterable<List<Char>> {
        val pSrc = keypad[srcChar]!!
        val pTgt = keypad[tgtChar]!!
        val dx = pTgt.x - pSrc.x
        val dy = pTgt.y - pSrc.y
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
        return moves.permutations()
            .toSet()
            .filter { allowed(keypad, pSrc, it) }
    }

    private fun countMovesKeypad(depth: Int, keypadSequence: List<Char>, f: (Int, Char, Char) -> Long): Long {
        return keypadSequence.zipWithNext { s, t -> f(depth, s, t) }.sum()
    }

    private val directionalCache = mutableMapOf<Triple<Int, Char, Char>, Long>()

    private fun bestDirectional(depth: Int, s: Char, t: Char): Long {
        val entry = Triple(depth, s, t)
        if (entry !in directionalCache) {
            directionalCache[entry] = if (depth == 0) {
                movesOnKeypad(positionsDirectionalKeypad, s, t).first().size + 1L
            } else {
                movesOnKeypad(positionsDirectionalKeypad, s, t)
                    .minOf { angebot -> countMovesKeypad(depth - 1, A + angebot + A, ::bestDirectional) }
            }
        }
        return directionalCache[entry]!!
    }

    private fun bestNumerical(depth: Int, s: Char, t: Char): Long {
        return movesOnKeypad(positionsNumericKeypad, s, t)
            .minOf { angebot -> countMovesKeypad(depth - 1, A + angebot + A, ::bestDirectional) }
    }

    private fun shortestButtonSequence(line: String, depth: Int): Long {
        val length = countMovesKeypad(depth, A + line.toList(), ::bestNumerical)
        val value = line.dropLast(1).toInt()
        return length * value
    }

    private fun sumAllButtonSequences(depth: Int): Long {
        return lines.sumOf { line -> shortestButtonSequence(line, depth) }
    }

    override fun part1(): Long {
        return sumAllButtonSequences(2)
    }

    override fun part2(): Long {
        return sumAllButtonSequences(25)
    }
}
