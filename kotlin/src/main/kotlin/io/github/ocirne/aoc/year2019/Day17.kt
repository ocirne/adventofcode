package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day17(val lines: List<String>) : AocChallenge(2019, 17) {

    private fun runProgram(program: IntCodeEmulator2019, print: Boolean=false): Map<Pair<Long, Long>, Char> {
        val scaffolds = mutableMapOf<Pair<Long, Long>, Char>()
        var x = 0L
        var y = 0L
        while (program.tick() != IntCodeEmulator2019.Companion.ReturnCode.STOP) {
            val c = program.getLastOutput().toInt().toChar()
            if (print) {
                print(c)
            }
            if (c == '\n') {
                y += 1
                x = 0
            } else {
                if (c == '#') {
                    scaffolds[x to y] = c
                }
                x += 1
            }
        }
        return scaffolds
    }

    fun findIntersections(scaffolds: Map<Pair<Long, Long>, Char>): Long {
        return scaffolds.filterKeys { (x, y) ->
            scaffolds[x - 1 to y] == '#' &&
            scaffolds[x + 1 to y] == '#' &&
            scaffolds[x to y - 1] == '#' &&
            scaffolds[x to y + 1] == '#'
        }.keys.sumOf { (x, y) -> x * y }
    }

    override fun part1(): Long {
        val scaffolds = runProgram(IntCodeEmulator2019(lines.first()))
        return findIntersections(scaffolds)
    }

    override fun part2(): Int {
        val penAndPaper = """B,A,B,C,A,B,C,A,B,C
            R,8,R,4,L,12
            L,12,L,12,L,6,L,6
            L,12,L,6,R,12,R,8
            n
            """
        val vacuum = IntCodeEmulator2019(lines.first())
        vacuum.program[0L] = 2L
        penAndPaper.filter { it != ' ' }.forEach { vacuum.addInput(it.code.toLong()) }
        runProgram(vacuum)
        return vacuum.getLastOutput().toInt()
    }
}
