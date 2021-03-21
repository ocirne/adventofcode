package io.github.ocirne.aoc.inputs

import com.opencsv.CSVParserBuilder
import com.opencsv.CSVReaderHeaderAware
import com.opencsv.CSVReaderHeaderAwareBuilder
import io.github.ocirne.aoc.AocChallenge
import org.junit.jupiter.api.TestInstance
import kotlin.reflect.KClass

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
internal class InputTestUtil {

    fun constructClass(dayClass: KClass<out AocChallenge>, year: String, dayNumber: String): AocChallenge {
        val content = this::class.java.classLoader
            .getResourceAsStream("$year/$dayNumber/input")!!
            .bufferedReader()
            .readLines()
        return dayClass.constructors.first().call(content)
    }

    fun load(year: String): Map<String, Map<String, String>> {
        println("read test data")
        val fileReader = this::class.java.classLoader.getResourceAsStream("results$year.csv")!!.bufferedReader()
        val csvParser = CSVParserBuilder().withSeparator(';').build()
        val reader = CSVReaderHeaderAwareBuilder(fileReader).withCSVParser(csvParser).build() as CSVReaderHeaderAware
        val resultMap = mutableMapOf<String, Map<String, String>>()
        var line = reader.readMap()
        while (line != null) {
            resultMap.put(line["day"]!!, line)
            line = reader.readMap()
        }
        return resultMap
    }
}
