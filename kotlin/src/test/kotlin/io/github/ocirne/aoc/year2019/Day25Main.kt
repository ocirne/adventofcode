package io.github.ocirne.aoc.year2019


fun main() {
    val droid = Droid()
    droid.play("")
    while (true) {
        val stringInput = readLine()!!
        droid.play(stringInput + "\n")
    }
}
