package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge

class Day15(val lines: List<String>) : AocChallenge(2023, 15) {

    fun aocHash(step: String): Int {
        return step.fold(0) { value, c -> (value + c.code) * 17 % 256 }
    }

    override fun part1(): Int {
        return lines.first().split(',').sumOf { step -> aocHash(step) }
    }

    fun focusingPower(boxes: List<LinkedHashMap<String, Int>>): Int {
        var result = 0
        boxes.mapIndexed { boxNumber, box ->
            box.onEachIndexed { slotNumber, (_, focalLength) ->
                result += (1 + boxNumber) * (slotNumber + 1) * focalLength
            }
        }
        return result
    }

    override fun part2(): Int {
        val boxes = (0..255).map { LinkedHashMap<String, Int>() }
        for (step in lines.first().split(',')) {
            val label = step.split("[=-]".toRegex()).first()
            val box = aocHash(label)
            if (step.contains("=")) {
                val focalLength = step.split("=").last().toInt()
                boxes[box][label] = focalLength
            } else if (step.endsWith('-')) {
                boxes[box].remove(label)
            }
        }
        return focusingPower(boxes)
    }
}
