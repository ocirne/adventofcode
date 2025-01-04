package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge

class Day9(val lines: List<String>) : AocChallenge(2024, 9) {

    val line = lines.firstOrNull()

//    TODO

    override fun part1(): Long {
        val disk = mutableListOf<Long?>()
        var flag = true
        var fi = 0L
        for (x in line!!.map { c -> c.digitToInt() }) {
            if (flag) {
                repeat(x) { disk.add(fi) }
                fi++
            } else {
                repeat(x) { disk.add(null) }
            }
            flag = !flag
        }
        println(disk)
        // compactify
        var np = disk.indexOfFirst { it == null }
        var lp = disk.lastIndex
        while (np <= lp) {
//            println("np $np lp $lp disk $disk")
            disk[np] = disk[lp]
            disk[lp] = null
            while (disk[np] != null) np++
            while (disk[lp] == null) lp--
        }
  //      println("np $np lp $lp disk $disk")
        // checksum
        return disk.filterNotNull().mapIndexed { index, file -> index * file }.sum()
    }

    data class File(val size: Int, val id: Long?)

    fun printDisk(disk: List<File>) {
        for (file in disk) {
            repeat(file.size) {print(file.id ?: '.')}
        }
        println()
    }

    override fun part2(): Long {
        val disk = mutableListOf<File>()
        var flag = true
        var fi = 0L
        for (x in line!!.map { c -> c.digitToInt() }) {
            if (flag) {
                disk.add(File(x, fi))
                fi++
            } else {
                disk.add(File(x, null))
            }
            flag = !flag
        }
//        println(disk)
        // compactify
        var fileId = disk.last().id!!
        var mp = disk.lastIndex
        while (fileId > 0L) {
//            printDisk(disk)
//            println(disk[mp])
            val needed = disk[mp].size
            val np = disk.indexOfFirst { file -> file.id == null && file.size >= needed }
            if (np != -1 && np < mp) {
                val freeSpace = disk[np].size
                disk[np] = File(needed, fileId)
                if (needed < freeSpace) {
                    disk.add(np + 1, File(freeSpace - needed, null))
                    mp++
                }
//                println("mp $mp ${disk[mp]} needed $needed")
                disk[mp] = File(needed, null)
            }
            fileId--
            while (disk[mp].id != fileId) {
                mp--
            }
        }
        printDisk(disk)
        // checksum
        var total = 0L
        var index = 0
        for (file in disk) {
            if (file.id == null) {
                index += file.size
                continue
            }
            repeat(file.size) {
                total += index * file.id
                index++
            }
        }
        return total
    }
}
