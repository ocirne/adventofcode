package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge

class Day15(val lines: List<String>) : AocChallenge(2023, 15) {

    fun aocHash(step: String): Int {
        return step.fold(0) { value, c -> (value + c.code) * 17 % 256 }
    }

    override fun part1(): Int {
        return lines.first().split(',').sumOf { step -> aocHash(step) }
    }

    fun focusingPower(boxes: List<MutableList<Pair<String, Int>>>): Int {
        var result = 0
        boxes.mapIndexed { boxNumber, box ->
            box.onEachIndexed { slotNumber, (_, focalLength) ->
                println("$boxNumber $slotNumber $focalLength")
                result += (1 + boxNumber) * (slotNumber + 1) * focalLength
            }
        }
        return result
    }

    override fun part2(): Int {
        val boxes = (0..255).map { mutableListOf<Pair<String, Int>>() }
        for (step in lines.first().split(',')) {
            if (step.contains("=")) {
                val label = step.split("=")[0]
                val box = aocHash(label)
                val focalLength = step.split("=")[1].toInt()
                var foo = true
                boxes[box].forEachIndexed { index, (iLabel, _) ->
                    if (iLabel == label) {
                        boxes[box][index] = label to focalLength
                        foo = false
                    }
                }
                if (foo) {
                    boxes[box].add(label to focalLength)
                }
            } else if (step.endsWith('-')) {
                val label = step.split("-")[0]
                val box = aocHash(label)
                boxes[box].removeIf { (iLabel, _) -> iLabel == label }
            } else {
                throw IllegalStateException()
            }
        }
        return focusingPower(boxes)
    }
}
