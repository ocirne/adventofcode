package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge

class Day19(val lines: List<String>) : AocChallenge(2023, 19) {

    companion object {
        private val IDENTIFIER_PATTERN = """[a-z]+""".toRegex()
        private val END_STATE_PATTERN = """[AR]""".toRegex()
        private val PART_PATTERN = """\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}""".toRegex()
        private val WORKFLOW_PATTERN = """([a-z]+)\{(.*)}""".toRegex()
        private val LESS_THAN_PATTERN = """([xmas])<(\d+):([ARa-z]+)""".toRegex()
        private val GREATER_THAN_PATTERN = """([xmas])>(\d+):([ARa-z]+)""".toRegex()
    }

    data class Part(val line: String) {

        val registers =
            "xmas".toCharArray()
                .zip(PART_PATTERN.find(line)!!.groupValues.drop(1).map { it.toInt() })
                .toMap()

        fun rating(): Int = registers.values.sum()
    }

    abstract class Rule(val nextWorkflow: String) {
        abstract fun match(part: Part): Boolean

        abstract fun anti(): Rule
    }

    class LessThanRule(val variable: Char, val value: Int, nextWorkflow: String) : Rule(nextWorkflow) {

        override fun match(part: Part): Boolean = part.registers[variable]!! < value

        override fun anti(): Rule = GreaterThanRule(variable, value - 1, "anti")
    }

    class GreaterThanRule(val variable: Char, val value: Int, nextWorkflow: String) :
        Rule(nextWorkflow) {

        override fun match(part: Part): Boolean = part.registers[variable]!! > value

        override fun anti(): Rule = LessThanRule(variable, value + 1, "anti")
    }

    class DirectRule(nextWorkflow: String) : Rule(nextWorkflow) {

        override fun match(part: Part): Boolean = true

        override fun anti(): Rule = this
    }

    class Workflow(rulesString: String) {

        val rules = rulesString.split(",").map { rule ->
            when {
                LESS_THAN_PATTERN.matches(rule) -> {
                    val (variable, value, nextWorkflow) = LESS_THAN_PATTERN.find(rule)!!.destructured
                    LessThanRule(variable.first(), value.toInt(), nextWorkflow)
                }

                GREATER_THAN_PATTERN.matches(rule) -> {
                    val (variable, value, nextWorkflow) = GREATER_THAN_PATTERN.find(rule)!!.destructured
                    GreaterThanRule(variable.first(), value.toInt(), nextWorkflow)
                }

                END_STATE_PATTERN.matches(rule) ->
                    DirectRule(rule)

                IDENTIFIER_PATTERN.matches(rule) ->
                    DirectRule(rule)

                else ->
                    throw IllegalStateException(rule)
            }
        }

        fun process(part: Part): String = rules.first { it.match(part) }.nextWorkflow
    }

    class Workflows(val lines: List<String>) {

        private val workflows: Map<String, Workflow>

        private val parts: List<Part>

        init {
            if (lines.isNotEmpty()) {
                val sep = lines.indexOf("")
                workflows = lines.subList(0, sep).associate { line ->
                    val (name, rules) = WORKFLOW_PATTERN.find(line)!!.destructured
                    name to Workflow(rules)
                }
                parts = lines.subList(sep + 1, lines.size).map { Part(it) }
            } else {
                workflows = mapOf()
                parts = listOf()
            }
        }

        private fun handlePart(part: Part): Boolean {
            var currentWorkflow = workflows["in"]!!
            while (true) {
                val result = currentWorkflow.process(part)
                if (result == "A")
                    return true
                if (result == "R")
                    return false
                currentWorkflow = workflows[result]!!
            }
        }

        fun sumAcceptedParts(): Int = parts.filter(::handlePart).sumOf { it.rating() }

        private fun upperBound(constraints: List<Rule>, category: Char): Int =
            constraints
                .filter { rule -> rule is LessThanRule && rule.variable == category }
                .minOfOrNull { (it as LessThanRule).value } ?: 4001

        private fun lowerBound(constraints: List<Rule>, category: Char): Int =
            constraints
                .filter { rule -> rule is GreaterThanRule && rule.variable == category }
                .maxOfOrNull { (it as GreaterThanRule).value } ?: 0

        private fun collectResult(collectedRules: List<Rule>): Long =
            "xmas".map { v -> upperBound(collectedRules, v) - lowerBound(collectedRules, v) - 1 }
                .map { it.toLong() }
                .reduce { acc, i -> acc * i }

        fun dfs(currentNode: String = "in", i: Int = 0, constraints: List<Rule> = listOf()): Long {
            if (currentNode == "A") {
                return collectResult(constraints)
            }
            if (currentNode == "R") {
                return 0
            }
            val currentWorkflow = workflows[currentNode]!!
            val currentRule = currentWorkflow.rules[i]
            // match
            var total = dfs(currentRule.nextWorkflow, 0, constraints + currentRule)
            // no match
            if (i + 1 < currentWorkflow.rules.size) {
                total += dfs(currentNode, i + 1, constraints + currentRule.anti())
            }
            return total
        }
    }

    private val workflows = Workflows(lines)

    override fun part1(): Int {
        return workflows.sumAcceptedParts()
    }

    override fun part2(): Long {
        return workflows.dfs()
    }
}
