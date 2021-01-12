
def run(data):
    floor = 0
    for index, b in enumerate(data):
        if b == '(':
            floor += 1
        elif b == ')':
            floor -= 1
        else:
            raise Exception
        if floor < 0:
            return index + 1


assert run(')') == 1
assert run('()())') == 5

data = open('input', 'r').readline()
print(run(data))
