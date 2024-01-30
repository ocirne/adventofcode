package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day22(val lines: List<String>) : AocChallenge(2019, 22) {

    abstract class Shuffler<T> {

        abstract fun dealIntoNewStack(acc: T): T

        abstract fun cutN(acc: T, n: Int): T

        abstract fun dealWithIncrementP(acc: T, p: Int): T

        fun applyOneLine(shuffle: String, acc: T): T {
            return when {
                shuffle == "deal into new stack" -> dealIntoNewStack(acc)
                shuffle.startsWith("cut") -> {
                    val n = shuffle.split(' ').last().toInt()
                    cutN(acc, n)
                }

                shuffle.startsWith("deal with increment") -> {
                    val p = shuffle.split(' ').last().toInt()
                    dealWithIncrementP(acc, p)
                }
                else -> throw IllegalArgumentException(shuffle)
            }
        }

        fun shuffle(lines: List<String>, accIn: T): T {
            var acc = accIn
            for (line in lines) {
                acc = applyOneLine(line, acc)
            }
            return acc
        }
    }

    private class NaiveShuffler: Shuffler<List<Int>>() {

        override fun dealIntoNewStack(acc: List<Int>): List<Int> {
            return acc.reversed()
        }

        override fun cutN(acc: List<Int>, n: Int): List<Int> {
            assert(n != 0)
            return if (n > 0) {
                acc.drop(n) + acc.take(n)
            } else {
                acc.drop(acc.size + n) + acc.take(acc.size + n)
            }
        }

        override fun dealWithIncrementP(acc: List<Int>, p: Int): List<Int> {
            val nextDeck = acc.toList().toMutableList()
            acc.indices.forEach { i ->
                nextDeck[(i * p) % acc.size] = acc[i]
            }
            return nextDeck
        }
    }

    private class MathShuffler(val m: Int): Shuffler<Int>() {

        override fun dealIntoNewStack(acc: Int): Int {
            return m - acc - 1
        }

        override fun cutN(acc: Int, n: Int): Int {
            return (acc - n).mod(m)
        }

        override fun dealWithIncrementP(acc: Int, p: Int): Int {
            return (acc * p).mod(m)
        }
    }

    fun naiveOneLine(shuffle: String, deck: IntRange): List<Int> {
        return NaiveShuffler().applyOneLine(shuffle, deck.toList())
    }

    fun naiveShuffler(deck: IntRange): List<Int> {
        return NaiveShuffler().shuffle(lines, deck.toList())
    }

    override fun part1(): Int {
        // return naiveShuffler(0..10_006).indexOf(2019)
        return MathShuffler(10_007).shuffle(lines, 2019)
    }

    val countCards = 119315717514047
    val countShuffle = 101741582076661

    override fun part2(): Int {
        return -1
    }
}