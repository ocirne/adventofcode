from functools import reduce

from aoc.util import load_input, load_example


class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "[%s,%s]" % (self.left, self.right)

    def __add__(self, other):
        return Pair(self, other)

    def explode(self, depth=0):
        if depth >= 4:
            return True, True, self.left.value, self.right.value

        left_done, replace, lefty, righty = self.left.explode(depth + 1)
        if left_done:
            if replace:
                self.left = Number(0)
                self.right.add_to_left(righty)
                return True, False, lefty, None
            if righty is not None:
                self.right.add_to_left(righty)
                return True, False, lefty, None
            return True, False, lefty, righty

        right_done, replace, lefty, righty = self.right.explode(depth + 1)
        if right_done:
            if replace:
                self.right = Number(0)
                self.left.add_to_right(lefty)
                return True, False, None, righty
            if lefty is not None:

                self.left.add_to_right(lefty)
                return True, False, None, righty
            return True, False, lefty, righty

        return False, False, None, None

    def add_to_left(self, value):
        self.left.add_to_left(value)

    def add_to_right(self, value):
        self.right.add_to_right(value)

    def split(self):
        if isinstance(self.left, Number):
            if self.left.value >= 10:
                x = self.left.value // 2
                self.left = Pair(Number(x), Number(self.left.value - x))
                return True
        else:
            if self.left.split():
                return True
        if isinstance(self.right, Number):
            if self.right.value >= 10:
                x = self.right.value // 2
                self.right = Pair(Number(x), Number(self.right.value - x))
                return True
        else:
            if self.right.split():
                return True
        return False

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def explode(self, unused):
        return False, False, None, None

    def add_to_left(self, value):
        self.value += value

    def add_to_right(self, value):
        self.value += value

    def magnitude(self):
        return self.value


def shunting_yard(sn):
    stack = []
    result = []
    number = ""
    for index, token in enumerate(sn):
        if token.isspace():
            continue
        elif token.isdigit():
            number += token
            if not sn[index + 1].isdigit():
                result.append(number)
                number = ""
        elif token == ",":
            while stack and stack[-1] == ",":
                result.append(stack.pop())
            stack.append(token)
        elif token == "[":
            stack.append(token)
        elif token == "]":
            while stack[-1] != "[":
                result.append(stack.pop())
            stack.pop()
    while stack:
        if stack[-1] == "]":
            raise
        result.append(stack.pop())
    return result


def evaluate(upn_stack):
    stack = []
    for token in upn_stack:
        if token.isdigit():
            stack.append(Number(int(token)))
        elif token == ",":
            right = stack.pop()
            left = stack.pop()
            stack.append(Pair(left, right))
        else:
            raise Exception
    return stack.pop()


def parse(sn):
    return evaluate(shunting_yard(sn))


def explode(sn):
    """
    >>> str(explode(parse('[[[[[9,8],1],2],3],4]')))
    '[[[[0,9],2],3],4]'
    >>> str(explode(parse('[7,[6,[5,[4,[3,2]]]]]')))
    '[7,[6,[5,[7,0]]]]'
    >>> str(explode(parse('[[6,[5,[4,[3,2]]]],1]')))
    '[[6,[5,[7,0]]],3]'
    >>> str(explode(parse('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')))
    '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    >>> str(explode(parse('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')))
    '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
    """
    sn.explode()
    return sn


def split(sn):
    """
    >>> str(split(parse('[[[[0,7],4],[15,[0,13]]],[1,1]]')))
    '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
    >>> str(split(parse('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')))
    '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
    """
    sn.split()
    return sn


def add(a, b):
    """
    >>> str(add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]'))
    '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
    """
    if not isinstance(a, Pair):
        a = parse(a)
    if not isinstance(b, Pair):
        b = parse(b)
    x = a + b
    while True:
        while True:
            done, _, _, _ = x.explode()
            if not done:
                break
        if not x.split():
            break
    return x


def add_list(numbers):
    """
    >>> str(add_list(['[1,1]', '[2,2]', '[3,3]', '[4,4]']))
    '[[[[1,1],[2,2]],[3,3]],[4,4]]'
    >>> str(add_list(['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]']))
    '[[[[3,0],[5,3]],[4,4]],[5,5]]'
    >>> str(add_list(['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]']))
    '[[[[5,0],[7,4]],[5,5]],[6,6]]'
    >>> str(add_list(load_example(__file__, '18a')))
    '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
    >>> str(add_list(load_example(__file__, '18b')))
    '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
    """
    if not isinstance(numbers[0], Pair):
        numbers = [parse(sn) for sn in numbers]
    return reduce(add, numbers)


def magnitude(sn):
    """
    >>> magnitude('[9,1]')
    29
    >>> magnitude('[1,9]')
    21
    >>> magnitude('[[9,1],[1,9]]')
    129
    >>> magnitude('[[1,2],[[3,4],5]]')
    143
    >>> magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    1384
    >>> magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]')
    445
    >>> magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]')
    791
    >>> magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]')
    1137
    >>> magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
    3488
    >>> magnitude('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
    4140
    """
    return parse(sn).magnitude()


def part1(lines):
    """
    >>> part1(load_example(__file__, "18b"))
    4140
    """
    return add_list(lines).magnitude()


def part2(lines):
    """
    >>> part2(load_example(__file__, "18b"))
    3993
    """
    return max(add(a, b).magnitude() for a in lines for b in lines)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "18")
    print(part1(data))
    print(part2(data))
