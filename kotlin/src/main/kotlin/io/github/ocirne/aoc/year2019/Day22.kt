package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day22(val lines: List<String>) : AocChallenge(2019, 22) {

    private fun dealIntoNewStack(deck: List<Int>): List<Int> {
        return deck.reversed()
    }

    private fun cutN(deck: List<Int>, n: Int): List<Int> {
        assert(n != 0)
        return if (n > 0) {
            deck.drop(n) + deck.take(n)
        } else {
            deck.drop(deck.size+n) + deck.take(deck.size+n)
        }
    }

    private fun dealWithIncrementP(deck: List<Int>, p: Int): List<Int> {
        val newDeck = deck.toList().toMutableList()
        deck.indices.forEach { i ->
            newDeck[(i*p) % deck.size] = deck[i]
        }
        return newDeck
    }

    fun bar2(shuffle: String, deck: List<Int>): List<Int> {
        return when {
            shuffle == "deal into new stack" -> dealIntoNewStack(deck)
            shuffle.startsWith("cut") -> {
                val n = shuffle.split(' ').last().toInt()
                cutN(deck, n)
            }
            shuffle.startsWith("deal with increment") -> {
                val p = shuffle.split(' ').last().toInt()
                dealWithIncrementP(deck, p)
            }
            else -> throw IllegalArgumentException(shuffle)
        }
    }

    fun bar(shuffle: String, deck: IntRange): List<Int> {
        return bar2(shuffle, deck.toList())
    }

    fun checkIntegrity(deck: List<Int>) {
        val m = mutableSetOf<Int>()
        for (n in deck) {
            if (m.contains(n)) {
                throw IllegalStateException()
            }
            m.add(n)
        }
    }

    fun foo(deckRange: IntRange): List<Int> {
        var deck = deckRange.toList()
        for (line in lines) {
            deck = bar2(line, deck)
            checkIntegrity(deck)
        }
        return deck
    }

    override fun part1(): Int {
        val deck = foo(0..10_006)
        return deck.indexOf(2019)
    }

    override fun part2(): Int {
        return -1
    }
}