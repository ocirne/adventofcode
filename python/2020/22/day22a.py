
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
