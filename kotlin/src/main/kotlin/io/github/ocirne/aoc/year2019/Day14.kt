package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

private const val CARGO_ORE = 1000000000000L

class Day14(val lines: List<String>) : AocChallenge(2019, 14) {

    data class Reaction(val name: String, val count: Long, val chemicals: Map<String, Long>)

    private fun readReactions(): List<Reaction> {
        return lines.map { line ->
            val (left, right) = line.split(" => ")
            val (quantity, product) = right.split(' ')
            val chemicals = left.split(", ").associate {
                val (c, n) = it.split(' ')
                n to c.toLong()
            }
            Reaction(product, quantity.toLong(), chemicals)
        }
    }

    private val reactions = if (lines.isNotEmpty()) readReactions() else listOf()

    private fun findMinimalOre(target: Long): Long {
        var chemicals = mapOf("FUEL" to target)
        while (chemicals.values.filter { it > 0 }.size > 1 || !chemicals.containsKey("ORE")) {
            val newChemicals = mutableMapOf<String, Long>()
            for ((rightName, rightCount) in chemicals.entries) {
                if (rightName == "ORE") {
                    val base = newChemicals.getOrDefault(rightName, 0)
                    newChemicals[rightName] = base + rightCount
                } else {
                    val r = reactions.single { it.name == rightName }
                    var factor = rightCount / r.count
                    var rest = rightCount % r.count
                    if (rest > 0) {
                        factor++
                        rest -= r.count
                    }
                    for ((leftName, leftCount) in r.chemicals.entries) {
                        val base = newChemicals.getOrDefault(leftName, 0)
                        newChemicals[leftName] = base + factor * leftCount
                    }
                    val base = newChemicals.getOrDefault(rightName, 0)
                    newChemicals[rightName] = base + rest
                }
            }
            chemicals = newChemicals
        }
        return chemicals["ORE"]!!
    }

    override fun part1(): Any {
        return findMinimalOre(1L)
    }

    private fun binarySearch(): Long {
        var left = 0L
        var right = CARGO_ORE
        var middle = 0L
        while (left <= right) {
            middle = (left + right) / 2
            val x = findMinimalOre(middle)
            if (x > CARGO_ORE) {
                 right = middle - 1
            } else {
                 left = middle + 1
            }
        }
        while (findMinimalOre(middle) > CARGO_ORE) {
            middle--
        }
        return middle
    }

    override fun part2(): Long {
        return binarySearch()
    }
}