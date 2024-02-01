package io.github.ocirne.aoc

import java.math.BigInteger
import java.math.BigInteger.*

fun exclusiveRange(f: Int, t: Int): IntRange = if (f < t) IntRange(f+1, t-1) else IntRange(t+1, f-1)

fun <T> Collection<T>.permutations(): Iterable<List<T>> {
    if (this.size <= 1) {
        return listOf(this.toList())
    }
    val result = ArrayList<List<T>>()
    this.forEach { value ->
        val rest = this.without(value)
        rest.permutations().forEach { permutation ->
            result.add(listOf(value) + permutation)
        }
    }
    return result
}

fun <T> Collection<T>.without(value: T): Collection<T> {
    val copy = this.toMutableSet()
    copy.remove(value)
    return copy.toSet()
}

fun <T> List<T>.combinationsOfTwo(): Sequence<Pair<T, T>> {
    val list = this
    return sequence {
        list.forEachIndexed { i, a ->
            list.subList(0, i).forEach { b ->
                yield(a to b)
            }
        }
    }
}

fun gcd(a: Int, b: Int): Int = if (b > 0) gcd(b, a % b) else a

fun gcd(a: Long, b: Long): Long = if (b > 0) gcd(b, a % b) else a

fun lcm(a: Int, b: Int): Int = a / gcd(a, b) * b

fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b

fun List<Int>.lcmList(): Int = this.reduce { acc, value -> lcm(acc, value) }

fun List<Long>.lcmList(): Long = this.reduce { acc, value -> lcm(acc, value) }

fun egcd(a: Long, b: Long): Triple<Long, Long, Long> {
    if (b == 0L) {
        return Triple(a, 1, 0)
    }
    val (d, s, t) = egcd(b, a % b)
    return Triple(d, t, s - (a / b) * t)
}

fun invMod(a: Long, n: Long): Long? {
    val (d, s, _) = egcd(a, n)
    if (d != 1L) {
        return null
    }
    return s.mod(n)
}
