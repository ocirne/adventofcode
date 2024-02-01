package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.math.BigInteger
import java.math.BigInteger.ONE
import java.math.BigInteger.valueOf

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
            return (- acc - 1).mod(m)
        }

        override fun cutN(acc: Int, n: Int): Int {
            return (acc - n).mod(m)
        }

        override fun dealWithIncrementP(acc: Int, p: Int): Int {
            return (acc * p).mod(m)
        }
    }

    private class MathShuffler2(val m: Long): Shuffler<Pair<Long, Long>>() {

        /**
         * x1 = a1 * x0 + b1
         * x2 = -x1 -1 = -1 * x1 - 1
         *
         * x2 = -1 * x1 - 1 = -1 * (a1 * x0 + b1) - 1 = -1 * a1 * x0 - b1 - 1 = -a1 * x0 + (-b1 - 1)
         */
        override fun dealIntoNewStack(acc: Pair<Long, Long>): Pair<Long, Long> {
            val (a1, b1) = acc
            return (-a1).mod(m) to (-b1-1).mod(m)
        }

        /**
         * x1 = a1 * x0 + b1
         * x2 = x1 - n
         *
         * x2 = x1 - n = (a1 * x0 + b1) - n = a1 * x0 + (b1 - n)
         */
        override fun cutN(acc: Pair<Long, Long>, n: Int): Pair<Long, Long> {
            val (a1, b1) = acc
            return a1 to (b1 - n).mod(m)
        }

        /**
         * x1 = a1 * x0 + b1
         * x2 = p * x1
         *
         * x2 = p * x1 = p * (a1 * x0 + b1) = p*a1 * x0 + p * b1
         *
         */
        override fun dealWithIncrementP(acc: Pair<Long, Long>, p: Int): Pair<Long, Long> {
            val (a1, b1) = acc
            return (p*a1).mod(m) to (p*b1).mod(m)
        }
    }

    fun naiveOneLine(shuffle: String, deck: IntRange): List<Int> {
        return NaiveShuffler().applyOneLine(shuffle, deck.toList())
    }

    fun naiveShuffler(deck: IntRange): List<Int> {
        return NaiveShuffler().shuffle(lines, deck.toList())
    }

    fun foo() {
        val a = 9778
        val b = 1192
        val deck = (0..10_006).toList()
        val shuffledDeck = naiveShuffler(0..10_006)
        for (i in 0..10_006) {
            assert(a * i + b == shuffledDeck[i])
        }
    }

    fun barCheck(deck: List<Int>, a: Int, b: Int): Boolean {
        for (i in 0..10_006) {
            val left = (a * i + b) % 10_007
            val right = MathShuffler(10_007).shuffle(lines, i)
//            val right = deck[(a * i + b) % 10_007]
            if (left != right) {
                println("$i: $left != $right")
           //     return false
            }
        }
        return true
    }

    fun bar() {
        val shuffledDeck = naiveShuffler(0..10_006)
        for (a in 3190..3190) {
            for (b in 180..180) {
                if (barCheck(shuffledDeck, a, b)) {
                    println("$a $b")
                }
            }
        }
    }

    override fun part1(): Long {
        val m = 10007L
        val index = 2019L
        // foo()
        //bar()
        // return naiveShuffler(0..10_006).indexOf(2019)
        //return MathShuffler(10_007).shuffle(lines, 2019)
        val (a, b) = MathShuffler2(m).shuffle(lines, 1L to 0L)

        return (a * index + b).mod(m)
    }

    override fun part2(): BigInteger {
        val mL = 119315717514047
        val m = valueOf(mL)
        val c = valueOf(101741582076661)
        val x = valueOf(2020L)
        val (aL, oL) = MathShuffler2(mL).shuffle(lines, 1L to 0L)
        val a = valueOf(aL)
        val b = valueOf(oL)
        val i = a.modInverse(m)
        val i2 = (i - ONE).modInverse(m)
        val r1 = x * i.modPow(c, m) % m
        val r2 = i.modPow(c + ONE, m) - i
        val r4 = (r2 * i2) % m
        val t = (r1 - b * r4).mod(m)
        return t
    }
}
