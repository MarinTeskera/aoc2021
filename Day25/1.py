f = open('Day25/input.txt', 'r')


def canMoveEast(lines, willMove):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '>':
                if j == len(lines[i]) - 1:
                    if lines[i][0] == '.':
                        willMove.append((i, j))
                else:
                    if lines[i][j + 1] == '.':
                        willMove.append((i, j))


def canMoveSouth(lines, willMove):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'v':
                if i == len(lines) - 1:
                    if lines[0][j] == '.':
                        willMove.append((i, j))
                else:
                    if lines[i + 1][j] == '.':
                        willMove.append((i, j))


def moveEast(lines, willMove):
    for i in willMove:
        (x, y) = i
        lines[x][y] = '.'

        if y == len(lines[0]) - 1:
            lines[x][0] = '>'
        else:
            lines[x][y + 1] = '>'


def moveSouth(lines, willMove):
    for i in willMove:
        (x, y) = i
        lines[x][y] = '.'

        if x == len(lines) - 1:
            lines[0][y] = 'v'
        else:
            lines[x + 1][y] = 'v'


l = f.readlines()
lines = [[j for j in i.strip()] for i in l]

n = 1

willMoveEast = []
willMoveSouth = []

canMoveEast(lines, willMoveEast)
moveEast(lines, willMoveEast)

canMoveSouth(lines, willMoveSouth)
moveSouth(lines, willMoveSouth)


while len(willMoveSouth) != 0 or len(willMoveEast) != 0:
    willMoveEast = []
    willMoveSouth = []

    canMoveEast(lines, willMoveEast)
    moveEast(lines, willMoveEast)

    canMoveSouth(lines, willMoveSouth)
    moveSouth(lines, willMoveSouth)
    n += 1

print(n)
