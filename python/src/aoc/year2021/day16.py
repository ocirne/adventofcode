from math import prod

from aoc.util import load_input


def pad(s):
    width = len(s)
    while width % 4 != 0:
        width += 1
    return s.rjust(width, "0")


def read_literal(binary, i):
    result = ""
    while True:
        print(binary[i : i + 5])
        result += binary[i + 1 : i + 5]
        if binary[i] == "0":
            break
        i += 5
    return int(result, 2), i + 5


def rest_is_zero(rest):
    return all(c == "0" for c in rest)


def read_package(binary, count_sub_packets=None):
    print("--> sub")
    i = 0
    j = 0
    version_sum = 0
    while i < len(binary) and (count_sub_packets is None or j < count_sub_packets):
        print("rest", binary[i:], "i", i, "j", j)
        if rest_is_zero(binary[i:]):
            return i, version_sum
        print("analyze", binary, i)
        version = int(binary[i : i + 3], 2)
        version_sum += version
        i += 3
        type_id = int(binary[i : i + 3], 2)
        i += 3
        print("version", version, "type_id", type_id)
        if type_id == 4:
            print("i", i)
            literal, i = read_literal(binary, i)
            print("literal", literal, i)
        else:
            length_type_id = binary[i]
            i += 1
            print("length_type_id", length_type_id)
            if length_type_id == "0":
                length_subpacket = int(binary[i : i + 15], 2)
                i += 15
                print("length_subpacket", length_subpacket)
                _, sub_version_sum = read_package(binary[i : i + length_subpacket])
                version_sum += sub_version_sum
                i += length_subpacket
            else:
                number_of_subpackets = int(binary[i : i + 11], 2)
                i += 11
                print("number of subpackets", number_of_subpackets)
                # the next 11 bits are a number that represents the number of sub-packets immediately contained by
                # this packet.
                done, sub_version_sum = read_package(binary[i:], 3)
                i += done
                version_sum += sub_version_sum
        print("done", "i", i)
        j += 1
    return i, version_sum


def decode_bits(bits):
    """
    >>> decode_bits('8A004A801A8002F478')
    16
    >>> decode_bits('620080001611562C8802118E34')
    12
    >>> decode_bits('C0015000016115A2E0802F182340')
    23
    >>> decode_bits('A0016C880162017C3686B18A3D4780')
    31
    """
    print(bits)
    binary = pad(bin(int(bits, 16))[2:])
    print(binary)
    i, vs = read_package(binary)
    print("return vs", vs)
    return vs


def part1(lines):
    return decode_bits(lines[0])


def read_package2(binary, count_sub_packets=None):
    print("--> sub")
    i = 0
    j = 0
    result = []
    while i < len(binary) and (count_sub_packets is None or j < count_sub_packets):
        print("rest", binary[i:], "i", i, "j", j)
        if rest_is_zero(binary[i:]):
            print("rest_is_zero")
            return i, result
        print("analyze", binary, i)
        version = int(binary[i : i + 3], 2)
        i += 3
        type_id = int(binary[i : i + 3], 2)
        i += 3
        print("version", version, "type_id", type_id)
        if type_id == 4:
            print("i", i)
            literal, i = read_literal(binary, i)
            print("literal", literal, i)
            result.append(literal)
        else:
            length_type_id = binary[i]
            i += 1
            print("length_type_id", length_type_id)
            if length_type_id == "0":
                length_subpacket = int(binary[i : i + 15], 2)
                i += 15
                print("length_subpacket", length_subpacket)
                _, sub_result = read_package2(binary[i : i + length_subpacket])
                i += length_subpacket
            else:
                number_of_subpackets = int(binary[i : i + 11], 2)
                i += 11
                print("number of subpackets", number_of_subpackets)
                # the next 11 bits are a number that represents the number of sub-packets immediately contained by
                # this packet.
                done, sub_result = read_package2(binary[i:], number_of_subpackets)
                i += done
            print("sub_result", sub_result)
            if type_id == 0:
                # sum of sub packages
                print("sum", sub_result)
                result.append(sum(sub_result))
            elif type_id == 1:
                # product of sub_packages
                result.append(prod(sub_result))
            elif type_id == 2:
                # minimum of sub_packages
                result.append(min(sub_result))
            elif type_id == 3:
                # maximum of sub_packages
                result.append(max(sub_result))
            elif type_id == 5:
                # greater than 1: frist is larger than two
                result.append(int(sub_result[0] > sub_result[1]))
            elif type_id == 6:
                # less than
                result.append(int(sub_result[0] < sub_result[1]))
            elif type_id == 7:
                # equal to
                print("equal", sub_result)
                result.append(int(sub_result[0] == sub_result[1]))

        print("done", "i", i)
        j += 1
    return i, result


def calc_bits(bits):
    """
    >>> calc_bits('C200B40A82')
    3
    >>> calc_bits('04005AC33890')
    54
    >>> calc_bits('880086C3E88112')
    7
    >>> calc_bits('CE00C43D881120')
    9
    >>> calc_bits('D8005AC2A8F0')
    1
    >>> calc_bits('F600BC2D8F')
    0
    >>> calc_bits('9C005AC2F8F0')
    0
    >>> calc_bits('9C0141080250320F1802104A08')
    1
    """
    print(bits)
    binary = pad(bin(int(bits, 16))[2:])
    print(binary)
    i, vs = read_package2(binary)
    print("return vs", vs)
    return vs[0]


def part2(lines):
    return calc_bits(lines[0])


if __name__ == "__main__":
    #    data = load_input(__file__, 2021, "16")
    #    assert decode_bits('D2FE28') == 0
    #    assert decode_bits('38006F45291200') == 16
    #    assert decode_bits('EE00D40C823060') == 16
    #    assert decode_bits("8A004A801A8002F478") == 16
    #    assert decode_bits("620080001611562C8802118E34") == 12
    #    assert decode_bits("C0015000016115A2E0802F182340") == 23
    #    assert decode_bits("A0016C880162017C3686B18A3D4780") == 31
    #    print(part1(data))

    #    assert calc_bits('C200B40A82') == 3
    #    assert calc_bits('04005AC33890') == 54
    #    assert calc_bits('880086C3E88112') == 7
    #    assert calc_bits('CE00C43D881120') == 9
    #    assert calc_bits('D8005AC2A8F0') == 1
    #    assert calc_bits('F600BC2D8F') == 0
    #    assert calc_bits('9C005AC2F8F0') == 0
    assert calc_bits("9C0141080250320F1802104A08") == 1
    print("--")
    data = load_input(__file__, 2021, "16")
    print(part2(data))

# wrong: 171452785237413100
