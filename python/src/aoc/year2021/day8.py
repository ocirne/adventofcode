from itertools import permutations

from aoc.util import load_input, load_example


def part1(lines):
    """
    >>> part1(load_example(__file__, "8"))
    26
    """
    result = 0
    for line in lines:
        signal_pattern, output_values = line.split("|")
        result += sum(1 for output_value in output_values.split() if len(output_value) in [2, 3, 4, 7])
    return result


A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6


def normalize_pattern(p):
    return "".join(sorted(p))


def generate_all_mappings():
    return [
        {
            # 0: abcefg
            normalize_pattern((m[A], m[B], m[C], m[E], m[F], m[G])): "0",
            # 1: cf
            normalize_pattern((m[C], m[F])): "1",
            # 2: acdeg
            normalize_pattern((m[A], m[C], m[D], m[E], m[G])): "2",
            # 3: acdfg
            normalize_pattern((m[A], m[C], m[D], m[F], m[G])): "3",
            # 4: bcdf
            normalize_pattern((m[B], m[C], m[D], m[F])): "4",
            # 5: abdfg
            normalize_pattern((m[A], m[B], m[D], m[F], m[G])): "5",
            # 6: abdefg
            normalize_pattern((m[A], m[B], m[D], m[E], m[F], m[G])): "6",
            # 7: acf
            normalize_pattern((m[A], m[C], m[F])): "7",
            # 8: abcdefg
            normalize_pattern((m[A], m[B], m[C], m[D], m[E], m[F], m[G])): "8",
            # 9: abcdfg
            normalize_pattern((m[A], m[B], m[C], m[D], m[F], m[G])): "9",
        }
        for m in list(permutations("abcdefg"))
    ]


def is_valid_mapping(mapping, patterns):
    return all(p in mapping for p in patterns)


def decode_output_values(mapping, output_values):
    return int("".join(mapping[v] for v in output_values))


def find_valid_mapping(all_mappings, line):
    signal_pattern, output_values = line.split("|")
    normalized_signal_pattern = [normalize_pattern(p) for p in signal_pattern.split()]
    normalized_output_values = [normalize_pattern(p) for p in output_values.split()]
    all_patterns = normalized_signal_pattern + normalized_output_values
    valid_mappings = [mapping for mapping in all_mappings if is_valid_mapping(mapping, all_patterns)]
    assert len(valid_mappings) == 1
    return decode_output_values(valid_mappings[0], normalized_output_values)


def part2(lines):
    """
    >>> part2(load_example(__file__, "8"))
    61229
    """
    all_mappings = generate_all_mappings()
    return sum(find_valid_mapping(all_mappings, line) for line in lines)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "8")
    print(part1(data))
    print(part2(data))
