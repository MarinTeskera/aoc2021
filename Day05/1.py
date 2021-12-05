f = open('Day05/input.txt', 'r')

matrix = []
x1List = []
x2List = []
y1List = []
y2List = []
xMax = 0
yMax = 0

for line in f.readlines():
    prvi, drugi = line.split(' -> ')
    x1, y1 = prvi.split(',')
    x2, y2 = drugi.split(',')

    if max(int(x1), int(x2)) + 1 > xMax:
        xMax = max(int(x1), int(x2)) + 1

    if max(int(y1), int(y2)) + 1 > yMax:
        yMax = max(int(y1), int(y2)) + 1

    x1List.append(x1)
    x2List.append(x2)
    y1List.append(y1)
    y2List.append(y2)

for i in range(yMax):
    matrix.append([])
    for j in range(xMax):
        matrix[i].append('.')

for i in range(len(x1List)):
    x1 = int(x1List[i])
    x2 = int(x2List[i])
    y1 = int(y1List[i])
    y2 = int(y2List[i])

    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            if matrix[j][x1] == '.':
                matrix[j][x1] = 1
            else:
                matrix[j][x1] += 1

    if y1 == y2:
        for j in range(min(x1, x2), max(x1, x2) + 1):
            if matrix[y1][j] == '.':
                matrix[y1][j] = 1
            else:
                matrix[y1][j] += 1

    if abs(x1 - x2) == abs(y1 - y2):
        if x1 > x2 and y1 > y2:
            for i in range(x1 - x2 + 1):
                if matrix[y1 - i][x1 - i] == '.':
                    matrix[y1 - i][x1 - i] = 1
                else:
                    matrix[y1 - i][x1 - i] += 1

        if x1 > x2 and y1 < y2:
            for i in range(x1 - x2 + 1):
                if matrix[y1 + i][x1 - i] == '.':
                    matrix[y1 + i][x1 - i] = 1
                else:
                    matrix[y1 + i][x1 - i] += 1

        if x1 < x2 and y1 > y2:
            for i in range(x2 - x1 + 1):
                if matrix[y1 - i][x1 + i] == '.':
                    matrix[y1 - i][x1 + i] = 1
                else:
                    matrix[y1 - i][x1 + i] += 1

        if x1 < x2 and y1 < y2:
            for i in range(x2 - x1 + 1):
                if matrix[y1 + i][x1 + i] == '.':
                    matrix[y1 + i][x1 + i] = 1
                else:
                    matrix[y1 + i][x1 + i] += 1

counter = 0

for i in matrix:
    for j in i:
        if j != '.' and j >= 2:
            counter += 1

print(counter)
