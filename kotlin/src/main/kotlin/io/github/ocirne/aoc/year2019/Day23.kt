package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day23(val lines: List<String>) : AocChallenge(2019, 23) {

    class NIC(lines: List<String>, val networkAddress: Long) {

        val program = IntCodeEmulator2019(lines.first()).addInput(networkAddress)

        fun tick(print: Boolean = false): Triple<Long, Long, Long>? {
            val rc = program.tick()
            return when (rc) {
                IntCodeEmulator2019.Companion.ReturnCode.STOP -> {
                    throw IllegalStateException("stop")
                }
                IntCodeEmulator2019.Companion.ReturnCode.NEED_INPUT -> {
                    program.addInput(-1)
                    null
                }
                else -> {
                    val da = program.getLastOutput()
                    program.tick()
                    val x = program.getLastOutput()
                    program.tick()
                    val y = program.getLastOutput()
//                    println("$networkAddress -> $da $x $y")
                    Triple(da, x, y)
                }
            }
        }
    }

    val network = mutableListOf<Triple<Long, Long, Long>>()

    override fun part1(): Long {
        val nics = IntRange(0, 49).map {  NIC(lines, it.toLong()) }
        while (true) {
            for (nic in nics) {
                if (network.isNotEmpty() && network.first().first == nic.networkAddress) {
                    val (_, x, y) = network.removeFirst()
                    nic.program.addInput(x)
                    nic.program.addInput(y)
                }
                val r = nic.tick(true)
                if (r != null) {
                    if (r.first == 255L) {
                        return r.third
                    }
                    network.add(r)
                }
            }
        }
    }

    override fun part2(): Long {
        var nat_x = 0L
        var nat_y = 0L
        var last_nat = -1L
        val nics = IntRange(0, 49).map {  NIC(lines, it.toLong()) }
        var i = 0
        while (true) {
            var active = false
            for (nic in nics) {
                if (network.isNotEmpty() && network.first().first == nic.networkAddress) {
                    val (_, x, y) = network.removeFirst()
                    nic.program.addInput(x)
                    nic.program.addInput(y)
                }
                val r = nic.tick(true)
                if (r != null) {
                    active = true
                    if (r.first == 255L) {
                        nat_x = r.second
                        nat_y = r.third
                    } else {
                        network.add(r)
                    }
                }
            }
            if (!active && network.isEmpty()) {
                if (nat_y == last_nat) {
                    return nat_y
                }
                last_nat = nat_y
                val nic = nics.first()
                nic.program.addInput(nat_x)
                nic.program.addInput(nat_y)
                println("nat -> 0 $nat_x $nat_y")
                i++
                if (i > 50) {
                    return -1
                }
            }
        }
    }
}
