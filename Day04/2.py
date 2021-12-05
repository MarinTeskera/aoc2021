def hasBingo(board, drawn):
    for i in board:
        count = 0

        for j in range(5):
            if (drawn.count(i[j]) > 0):
                i[j] = 0

        if (i.count(0) == 5):
            return True

    transp = [[], [], [], [], []]

    for i in range(5):
        for j in range(5):
            transp[i].append(board[j][i])

    for i in transp:
        count = 0

        for j in range(5):
            if (drawn.count(i[j]) > 0):
                i[j] = 0
                count += 1

        if (i.count(0) == 5):
            return True

    return False


f = open('Day04/input.txt', 'r')

boards = [[]]
cnt = 0

drawing = f.readline().split(',')
f.readline()

b = f.readlines()

for i in range(len(b)):
    line = b[i].split()

    if (line != []):
        boards[cnt].append(line)
    elif (line == []):
        cnt += 1
        boards.append([])

draw = []
rj = []
winners = []

for i in range(5, len(drawing)):
    draw = drawing[0:i]

    for board in boards:
        if (hasBingo(board, draw) and len(boards) == 1):
            print(board)
            rj = board
            boards.remove(board)
            break

        elif (hasBingo(board, draw)):
            boards.remove(board)

    if (len(boards) == 0):
        break

suma = 0

for i in rj:
    print(i)
    for j in i:
        if (j != 0):
            suma += int(j)

print(suma * int(draw[-1]))
