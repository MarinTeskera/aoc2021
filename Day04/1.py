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
exit = 0

for i in range(5, len(drawing)):
    draw = drawing[0:i]

    for board in boards:
        if (hasBingo(board, draw)):
            exit = 1
            rj = board
            break
    if(exit):
        break

suma = 0

for i in rj:
    for j in i:
        if (j != 0):
            suma += int(j)

mul = draw[-1]

pov = suma * mul

print(mul, '\n')
print(rj)
print(suma * int(mul))
