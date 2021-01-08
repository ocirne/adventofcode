
def puzzleInput(filename):
    path = '../../../adventofcode-input/' + filename
    file = open(path, 'r')
    return file.readlines()
