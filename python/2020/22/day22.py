
from collections import deque


def readData(filename):
    f = open(filename, 'r')
    cards1 = deque()
    cards2 = deque()
    for line in f.readlines():
        if line.isspace():
            continue
        elif line.startswith('Player'):
            player = int(line.split()[1].split(':')[0])
        else:
            num = int(line)
            if player == 1:
                cards1.append(num)
            else:
                cards2.append(num)
    return cards1, cards2


def turn(cards1, cards2):
    val1 = cards1.popleft()
    val2 = cards2.popleft()
    if val1 > val2:
        cards1.append(val1)
        cards1.append(val2)
    else:
        cards2.append(val2)
        cards2.append(val1)


def calcScore(cards):
    return sum((i+1) * cards.pop() for i in range(len(cards)))


def run(filename):
    cards1, cards2 = readData(filename)
    while True:
        turn(cards1, cards2)
        if len(cards1) == 0:
            return calcScore(cards2)
        if len(cards2) == 0:
            return calcScore(cards1)


assert run('reference') == 306

print(run('input'))



if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

from collections import deque


def readData(filename):
    f = open(filename, 'r')
    cards1 = deque()
    cards2 = deque()
    for line in f.readlines():
        if line.isspace():
            continue
        elif line.startswith('Player'):
            player = int(line.split()[1].split(':')[0])
        else:
            num = int(line)
            if player == 1:
                cards1.append(num)
            else:
                cards2.append(num)
    return cards1, cards2


def calcScore(cards):
    return sum((i+1) * cards.pop() for i in range(len(cards)))


def game(cards1, cards2):
    history_cards1 = {}
    history_cards2 = {}
    while True:
        val1 = cards1.popleft()
        val2 = cards2.popleft()
        if val1 <= len(cards1) and val2 <= len(cards2):
            winner, _ = game(deque(list(cards1)[:val1]), deque(list(cards2)[:val2]))
        elif val1 > val2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            cards1.append(val1)
            cards1.append(val2)
        else:
            cards2.append(val2)
            cards2.append(val1)

        if tuple(cards1) in history_cards1:
            return 1, cards1
        if tuple(cards2) in history_cards2:
            return 1, cards1
        if len(cards1) == 0:
            return 2, cards2
        if len(cards2) == 0:
            return 1, cards1
        history_cards1[tuple(cards1)] = True
        history_cards2[tuple(cards2)] = True


def run(filename):
    cards1, cards2 = readData(filename)
    winner, cards = game(cards1, cards2)
    score = calcScore(cards)
    return score


assert run('reference') == 291

print(run('input'))
