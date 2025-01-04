package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day23(val lines: List<String>) : AocChallenge(2024, 23) {

    override fun part1(): Int {
        val pairs = lines.map { it.trim().split('-').toSet() }
        val nList = pairs.flatten().toSet()
        val tList = nList.filter { it.startsWith('t') }.toSet()
        val result = mutableSetOf<Set<String>>()
        for (t in tList) {
            for (p in pairs) {
                if (t in p)
                    continue
                val (a, b) = p.toList()
                if (setOf(a, t) in pairs && setOf(b, t) in pairs) {
                    result.add(setOf(t, a, b))
                }
            }
        }
        return result.size
    }

    private fun isConnected(allPairs: Set<Set<String>>, t: String, s: Set<String>): Boolean {
        if (t in s)
            return false
        for (a in s) {
            if (setOf(a, t) !in allPairs) {
                return false
            }
        }
        return true
    }

    private fun allTriples(allPairs: Set<Set<String>>, allSets: Set<Set<String>>): String {
        if (allSets.size == 1) {
            return allSets.first().sorted().joinToString(",")
        }
        val tList = allSets.flatten().toSet()
        val result = mutableSetOf<Set<String>>()
        for (t in tList) {
            for (s in allSets) {
                if (isConnected(allPairs, t, s)) {
                    result.add(s + t)
                }
            }
        }
        return allTriples(allPairs, result)
    }

    override fun part2(): String {
        val pairs = lines.map { it.trim().split('-').toSet() }.toSet()
        return allTriples(pairs, pairs)
    }
}
