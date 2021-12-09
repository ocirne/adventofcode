def simulate(a):
    result = ""
    d = a + 4 * 643
    while True:
        a = d
        while a != 0:
            print(a, d)
            b = a
            a = 0
            x = True
            while x:
                c = 2
                while True:
                    if b == 0:
                        x = False
                        break
                    b -= 1
                    c -= 1
                    if c == 0:
                        break
                if x:
                    a += 1

            result += str(2 - c)
            if len(result) > 100:
                return result


def part1():
    for i in range(1000):
        result = simulate(i)
        if result.startswith("0101010101010101"):
            return i


if __name__ == "__main__":
    print(part1())
