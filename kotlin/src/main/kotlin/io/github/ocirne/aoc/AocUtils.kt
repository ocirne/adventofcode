package io.github.ocirne.aoc

fun <T> Collection<T>.permutations(): Iterable<List<T>> {
    if (this.size <= 1) {
        return listOf(this.toList())
    }
    val result = ArrayList<List<T>>()
    this.forEach { value ->
        val rest = this.without(value)
        rest.permutations().forEach { permutation ->
            result.add(listOf(value) + permutation)
        }
    }
    return result
}

fun <T> Collection<T>.without(value: T): Collection<T> {
    val copy = this.toMutableSet()
    copy.remove(value)
    return copy.toSet()
}
