package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day14(val lines: List<String>) : AocChallenge(2019, 14) {

    data class Reaction(val name: String, val count: Long, val chemicals: Map<String, Long>)

    override fun part1(): Long {
        val reactions = mutableListOf<Reaction>()
        for (line in lines) {
            val (chemicalsString, product) = line.split(" => ")
            val (quantity, name) = product.split(' ')
            val chemicals = mutableMapOf<String, Long>()
            for (x in chemicalsString.split(", ")) {
                val (c, n) = x.split(' ')
                chemicals[n] = c.toLong()
            }
            val r = Reaction(name, quantity.toLong(), chemicals)
            reactions.add(r)
        }
        var foo = reactions.filter { it.name == "FUEL" }.single()
        var t = 0
        while (foo.chemicals.values.filter { it > 0 }.size > 1 || !foo.chemicals.containsKey("ORE")) {
            t++
            if (t > 20) {
                return -1
            }
            println(foo)
            val newChemicals = mutableMapOf<String, Long>()
            for ((p_name, p_count) in foo.chemicals.entries) {
                if (p_name == "ORE") {
                    val base = newChemicals.getOrDefault(p_name, 0)
                    newChemicals.put(p_name, base + p_count)
                } else if (reactions.any { it.name == p_name }) {
                    val r = reactions.single { it.name == p_name }
                    var c = p_count
                    // TODO modulo?
                    while (c > 0) {
                        for ((n2, c2) in r.chemicals.entries) {
                            val base = newChemicals.getOrDefault(n2, 0)
                            newChemicals.put(n2, base + c2)
                        }
                        c -= r.count
                    }
                    val base = newChemicals.getOrDefault(p_name, 0)
                    newChemicals.put(p_name, base + c)
                } else {
                    throw IllegalStateException(p_name)
                }
            }
            foo = Reaction(foo.name, foo.count, newChemicals)
        }
        println(foo)

        println("result: ${foo.chemicals["ORE"]}")
        return foo.chemicals["ORE"]!!
    }

    fun betterPart1(target: Long): Long {

        val reactions = mutableListOf<Reaction>()
        for (line in lines) {
            val (chemicalsString, product) = line.split(" => ")
            val (quantity, name) = product.split(' ')
            val chemicals = mutableMapOf<String, Long>()
            for (x in chemicalsString.split(", ")) {
                val (c, n) = x.split(' ')
                chemicals[n] = c.toLong()
            }
            val r = Reaction(name, quantity.toLong(), chemicals)
            reactions.add(r)
        }
        reactions.add(Reaction("TARGET", 1, mapOf("FUEL" to target)))
        var foo = reactions.filter { it.name == "TARGET" }.single()
        while (foo.chemicals.values.filter { it > 0 }.size > 1 || !foo.chemicals.containsKey("ORE")) {
            val newChemicals = mutableMapOf<String, Long>()
            for ((p_name, p_count) in foo.chemicals.entries) {
                if (p_name == "ORE") {
                    val base = newChemicals.getOrDefault(p_name, 0)
                    newChemicals.put(p_name, base + p_count)
                } else if (reactions.any { it.name == p_name }) {
                    val r = reactions.single { it.name == p_name }
                    var factor = p_count / r.count
                    var rest = p_count % r.count
                    if (rest > 0) {
                        factor++
                        rest -= r.count
                    }
                    for ((n2, c2) in r.chemicals.entries) {
                        val base = newChemicals.getOrDefault(n2, 0)
                        newChemicals.put(n2, base + factor * c2)
                    }
                    val base = newChemicals.getOrDefault(p_name, 0)
                    newChemicals.put(p_name, base + rest)
                } else {
                    throw IllegalStateException(p_name)
                }
            }
            foo = Reaction(foo.name, foo.count, newChemicals)
        }
        println("result: ${foo.chemicals["ORE"]}")
        return foo.chemicals["ORE"]!!
    }

    fun binarySearch(): Long {
        var left = 0L
        var right = 1000000000000L
        var middle = 0L
        while (left < right) {
            middle = (left + right) / 2
            print("$left $middle $right")
            val x = betterPart1(middle)
            if (x > 1000000000000L) {
                 right = middle - 1
            } else {
                 left = middle + 1
            }
        }
        while (betterPart1(middle) > 1000000000000L) {
            middle--
        }
        println(middle)
        println("0 ${betterPart1(middle)}")
        println("+1 ${betterPart1(middle+1)}")
        println("+2 ${betterPart1(middle+2)}")
        println("+3 ${betterPart1(middle+3)}")
        // TODO Warum +1?
        return middle + 1
    }

    override fun part2(): Long {
        return binarySearch()
    }
}