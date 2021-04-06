package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge

class Day7(val lines: List<String>) : AocChallenge(2015, 7) {

    override fun part1(): Int {
        return run("a")
    }

    override fun part2(): Int {
        val answer1 = part1()
        return run("a", answer1.toString())
    }

    private fun prepareRules(newRuleB : String?): Map<String, Node> {
        return lines.map { it.trim().split(" -> ") }
            .map { Pair(it[1], if (it[1] == "b" && newRuleB != null) Node(newRuleB) else Node(it[0])) }
            .toMap()
    }

    fun run(wire: String, newRuleB : String? = null): Int {
        val rules = prepareRules(newRuleB)
        return Circuit(rules).deduct(wire)
    }

    internal class Circuit(private val rules: Map<String, Node>) {

        internal fun deduct(wire: String): Int {
            if (wire.toIntOrNull() != null) {
                return wire.toInt()
            }
            val node = rules[wire]!!
            if (node.value != 0) {
                return node.value
            }
            when (node.rule.size) {
                1 -> {
                    node.value = deduct(node.rule[0])
                }
                2 -> {
                    val (op, ref) = node.rule
                    if (op == "NOT") {
                        node.value = M - 1 - deduct(ref)
                    }
                }
                3 -> {
                    val (ref1, op, ref2) = node.rule
                    val value1 = deduct(ref1)
                    val value2 = deduct(ref2)
                    node.value = when (op) {
                        "AND" -> value1 and value2
                        "OR" -> value1 or value2
                        "LSHIFT" -> value1 shl value2
                        "RSHIFT" -> value1 shr value2
                        else -> throw Exception()
                    }
                }
            }
            return node.value
        }
    }

    internal class Node(tokens: String) {
        val rule = tokens.split(' ')
        var value : Int = 0
    }

    companion object {
        // 2 ^ 16
        const val M = 1 shl 16
    }
}
