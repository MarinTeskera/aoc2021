f = open('Day20/input.txt', 'r')


def pixelNum(picture, i, j):
    bin = ''

    for (x, y) in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if picture[x][y] == '#':
            bin += '1'
        else:
            bin += '0'

    return bin


def apply(picture, alg):
    for i in range(1, len(picture) - 1):
        for j in range(1, len(picture[i]) - 1):
            picture[i][j] = alg[int(pixelNum(picture, i, j), 2)]


alg = f.readline().strip()
f.readline()
picture = []

for i in f.readlines():
    picture.append(['.']+[j for j in i.strip()]+['.'])

picture.append(['.'] * 17)
picture.insert(0, ['.'] * 17)

for i in picture:
    print(*i)
print()

for i in range(2):
    apply(picture, alg)
    for j in picture:
        print(*j)
    print()

cnt = 0
for i in picture:
    cnt += i.count('#')


print(cnt)
