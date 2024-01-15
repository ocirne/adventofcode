package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.year2019.IntCodeEmulator2019.Companion.ReturnCode

class Droid {

    private val droid = IntCodeEmulator2019(loadProgram())

    fun play(input: String) {
        input.forEach { droid.addInput(it.code.toLong()) }
        while (droid.tick() != ReturnCode.STOP) {
            print(droid.getLastOutput().toInt().toChar())
            if (droid.getLastOutput() == '?'.code.toLong()) {
                return
            }
        }
    }

    companion object {
        fun loadProgram(): String {
            return this::class.java.classLoader.getResourceAsStream("inputs/2019/25/input")!!.bufferedReader()
                .readLines().map { it.trim() }.first()
        }
    }
}
