package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.max

class Day22(val lines: List<String>) : AocChallenge(2024, 22) {

    private fun evolveNumber(x0: Long): Long {
        val x1 = ((x0 * 64) xor x0).mod(16777216L)
        val x2 = ((x1 / 32) xor x1).mod(16777216L)
        val x3 = ((x2 * 2048) xor x2).mod(16777216L)
        return x3
    }

    fun foo(x: Long): Long {
        var sn = x
        repeat(2000) { sn = evolveNumber(sn) }
        return sn
    }

    override fun part1(): Long {
        var total = 0L
        for (line in lines) {
            val x = foo(line.toLong())
  //          println(x)
            total += x
        }
        return total
    }

    fun bar(x: Long): Sequence<Pair<String, Int>> {
        return sequence {
            var last_value = x
            val queue = mutableListOf<Int>()
            repeat(4) {
                val value = evolveNumber(last_value)
                val delta = value.mod(10) - last_value.mod(10)
                queue.add(delta)
                last_value = value
//                println("[init] delta " + delta + ", queue " + queue)
            }
            yield(queue.joinToString(",") to last_value.mod(10))
            repeat(1996) {
                val value = evolveNumber(last_value)
                val delta = value.mod(10) - last_value.mod(10)
                queue.removeFirst()
                queue.add(delta)
                last_value = value
                yield(queue.joinToString(",") to value.mod(10))
            }
        }
    }

    override fun part2(): Int {
        val totalMap = mutableMapOf<String, Int>()
        for (line in lines) {
            val localBest = mutableMapOf<String, Int>()
            for ((queue, value) in bar(line.toLong())) {
//                println("" + queue + " -- " + value)
                if (queue !in localBest) {
//                    println("" + queue + " " + value)
//                    localBest.computeIfPresent(queue) { _, b -> max(value, b) }
//                } else {
                    localBest.put(queue, value)
                }
            }
//            println("best " + best)
//            println("foo " + best["-2,1,-1,3"])
            for ((key, value) in localBest) {
                if (key in totalMap) {
                    totalMap[key] = totalMap[key]!! + value
                } else {
                    totalMap[key] = value
                }
            }
//            total += x
        }
//        println("totalMap " + totalMap)
//        println("bar " + totalMap["-2,1,-1,3"])
        return totalMap.values.max()
    }
}
