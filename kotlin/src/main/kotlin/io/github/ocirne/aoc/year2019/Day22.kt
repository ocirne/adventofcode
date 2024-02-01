package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge
import java.math.BigInteger
import java.math.BigInteger.*

class Day22(val lines: List<String>) : AocChallenge(2019, 22) {

    abstract class Shuffler<T> {

        abstract fun dealIntoNewStack(acc: T): T

        abstract fun cutN(acc: T, n: Int): T

        abstract fun dealWithIncrementP(acc: T, n: Int): T

        fun applyOneLine(shuffle: String, acc: T): T {
            if (shuffle.startsWith("deal into new stack")) {
                return dealIntoNewStack(acc)
            }
            val n = shuffle.split(' ').last().toInt()
            return if (shuffle.startsWith("cut")) {
                cutN(acc, n)
            } else { // must be startsWith("deal with increment")
                dealWithIncrementP(acc, n)
            }
        }

        fun shuffle(lines: List<String>, accIn: T): T {
            return lines.fold(accIn) { acc, line -> applyOneLine(line, acc) }
        }
    }

    private class IntShuffler(val m: Int): Shuffler<Pair<Int, Int>>() {

        override fun dealIntoNewStack(acc: Pair<Int, Int>): Pair<Int, Int> {
            val (a, b) = acc
            return (-a).mod(m) to (-b-1).mod(m)
        }

        override fun cutN(acc: Pair<Int, Int>, n: Int): Pair<Int, Int> {
            val (a, b) = acc
            return a to (b - n).mod(m)
        }

        override fun dealWithIncrementP(acc: Pair<Int, Int>, n: Int): Pair<Int, Int> {
            val (a, b) = acc
            return (n*a).mod(m) to (n*b).mod(m)
        }
    }

    private class BigIntegerShuffler(val m: BigInteger): Shuffler<Pair<BigInteger, BigInteger>>() {

        override fun dealIntoNewStack(acc: Pair<BigInteger, BigInteger>): Pair<BigInteger, BigInteger> {
            val (a, b) = acc
            return (-a).mod(m) to (-b- ONE).mod(m)
        }

        override fun cutN(acc: Pair<BigInteger, BigInteger>, n: Int): Pair<BigInteger, BigInteger> {
            val (a, b) = acc
            return a to (b - valueOf(n.toLong())).mod(m)
        }

        override fun dealWithIncrementP(acc: Pair<BigInteger, BigInteger>, n: Int): Pair<BigInteger, BigInteger> {
            val (a, b) = acc
            val bn = valueOf(n.toLong())
            return (bn*a).mod(m) to (bn*b).mod(m)
        }
    }

    override fun part1(): Int {
        val m = 10007
        val index = 2019
        val (a, b) = IntShuffler(m).shuffle(lines, 1 to 0)
        return (a * index + b).mod(m)
    }

    override fun part2(): BigInteger {
        val m = valueOf(119315717514047)
        val c = valueOf(101741582076661)
        val x = valueOf(2020L)
        val (a, b) = BigIntegerShuffler(m).shuffle(lines, ONE to ZERO)
        val i = a.modInverse(m)
        return (x * i.modPow(c, m) - b * ((i.modPow(c + ONE, m) - i) * (i - ONE).modInverse(m))).mod(m)
    }
}
