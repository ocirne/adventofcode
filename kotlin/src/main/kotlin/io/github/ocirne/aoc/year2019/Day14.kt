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

    override fun part2(): Int {
        return -1
    }
}
