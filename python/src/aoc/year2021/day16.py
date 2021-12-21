from math import prod

from aoc.util import load_input


def read_bits(bits):
    """
    >>> read_bits('D2FE28')
    '110100101111111000101000'
    >>> read_bits('38006F45291200')
    '00111000000000000110111101000101001010010001001000000000'
    >>> read_bits('04005AC33890')
    '000001000000000001011010110000110011100010010000'
    """
    return "".join(bin(int(c, 16))[2:].rjust(4, "0") for c in bits.strip())


def read_literal(binary, i):
    result = ""
    while True:
        result += binary[i + 1 : i + 5]
        if binary[i] == "0":
            break
        i += 5
    return int(result, 2), i + 5


def rest_is_zero(rest):
    return all(c == "0" for c in rest)


def analyze_packages(binary, count_sub_packets=None):
    i = 0
    j = 0
    version_sum = 0
    result = []
    while i < len(binary) and (count_sub_packets is None or j < count_sub_packets):
        if rest_is_zero(binary[i:]):
            return i, version_sum, result
        version = int(binary[i : i + 3], 2)
        version_sum += version
        i += 3
        type_id = int(binary[i : i + 3], 2)
        i += 3
        if type_id == 4:
            literal, i = read_literal(binary, i)
            result.append(literal)
        else:
            length_type_id = binary[i]
            i += 1
            if length_type_id == "0":
                length_subpacket = int(binary[i : i + 15], 2)
                i += 15
                _, sub_version_sum, sub_result = analyze_packages(binary[i : i + length_subpacket])
                i += length_subpacket
                version_sum += sub_version_sum
            else:
                number_of_subpackets = int(binary[i : i + 11], 2)
                i += 11
                done, sub_version_sum, sub_result = analyze_packages(binary[i:], number_of_subpackets)
                i += done
                version_sum += sub_version_sum
            if type_id == 0:
                result.append(sum(sub_result))
            elif type_id == 1:
                result.append(prod(sub_result))
            elif type_id == 2:
                result.append(min(sub_result))
            elif type_id == 3:
                result.append(max(sub_result))
            elif type_id == 5:
                result.append(int(sub_result[0] > sub_result[1]))
            elif type_id == 6:
                result.append(int(sub_result[0] < sub_result[1]))
            elif type_id == 7:
                result.append(int(sub_result[0] == sub_result[1]))
        j += 1
    return i, version_sum, result


def part1(lines):
    """
    >>> part1(['8A004A801A8002F478'])
    16
    >>> part1(['620080001611562C8802118E34'])
    12
    >>> part1(['C0015000016115A2E0802F182340'])
    23
    >>> part1(['A0016C880162017C3686B18A3D4780'])
    31
    """
    binary = read_bits(lines[0])
    _, version_sum, _ = analyze_packages(binary)
    return version_sum


def part2(lines):
    """
    >>> part2(['C200B40A82'])
    3
    >>> part2(['04005AC33890'])
    54
    >>> part2(['880086C3E88112'])
    7
    >>> part2(['CE00C43D881120'])
    9
    >>> part2(['D8005AC2A8F0'])
    1
    >>> part2(['F600BC2D8F'])
    0
    >>> part2(['9C005AC2F8F0'])
    0
    >>> part2(['9C0141080250320F1802104A08'])
    1
    """
    binary = read_bits(lines[0])
    _, _, result = analyze_packages(binary)
    return result[0]


if __name__ == "__main__":
    data = load_input(__file__, 2021, "16")
    print(part1(data))
    print(part2(data))
