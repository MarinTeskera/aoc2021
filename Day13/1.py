f = open('Day13/input.txt', 'r')


def printDots(dots):
    for i in dots:
        s = ''
        for j in i:
            if j == '.':
                s += ' '
            else:
                s += '@'
        print(s)


def countDots(dots):
    cnt = 0
    for i in dots:
        cnt += i.count('#')

    return cnt


def foldY(dots, location):
    if location == len(dots) // 2:
        for i in range(location):
            for j in range(len(dots[0])):
                if dots[location - 1 - i][j] == '#' or dots[location + 1 + i][j] == '#':
                    dots[location - 1 - i][j] = '#'
        for i in range(location, len(dots)):
            dots.pop(location)

    elif location > len(dots) // 2:
        for i in range(len(dots) - 1 - location):
            for j in range(len(dots[0])):
                if dots[location - 1 - i][j] == '#' or dots[location + 1 + i][j] == '#':
                    dots[location - 1 - i][j] = '#'
        for i in range(location, len(dots)):
            dots.pop(location)

    elif location < len(dots) // 2:
        n = len(dots) - len(dots) // 2 - location
        new = []
        for i in range(n, 0, -1):
            new.append(dots[-i])
        for i in range(location):
            for j in range(len(dots[0])):
                if dots[location - 1 - i][j] == '#' or dots[location + 1 + i][j] == '#':
                    dots[location - 1 - i][j] = '#'
        for i in range(location, len(dots)):
            dots.pop(location)
        for i in new:
            dots.insert(0, i)


def foldX(dots, location):
    condition = location == len(dots[0])//2
    if condition:
        for i in range(location):
            for j in range(len(dots)):
                if dots[j][location - 1 - i] == '#' or dots[j][location + 1 + i] == '#':
                    dots[j][location - 1 - i] = '#'
        for i in range(len(dots)):
            while len(dots[i]) > location:
                dots[i].pop(location)

    elif location > len(dots[0]) // 2:
        for k in range(len(dots)):
            i = location - 1
            j = location + 1
            while i >= 0 and j < len(dots[k]):
                if dots[k][i] == '#' or dots[k][j] == '#':
                    dots[k][i] = '#'
                i -= 1
                j += 1
        for i in range(len(dots)):
            while len(dots[i]) > location:
                dots[i].pop(location)

    elif location < len(dots[0]) // 2:
        n = len(dots) - len(dots[0]) // 2 - location
        new = []
        for i in range(len(dots)):
            l = dots[i][n:len(dots[i])]
            new.append(l)

        for k in range(len(dots)):
            i = location - 1
            j = location + 1
            while i >= 0 and j < len(dots[k]):
                if dots[k][i] == '#' or dots[k][j] == '#':
                    dots[k][i] = '#'
                i -= 1
                j += 1
        for i in range(len(dots)):
            while len(dots[i]) > location:
                dots[i].pop(location)
            for j in new[i]:
                dots[i].insert(0, j)


lines = f.readlines()

x = []
y = []
dots = []

line = 0
while lines[line] != '\n':
    a, b = lines[line].strip().split(',')
    x.append(int(a))
    y.append(int(b))
    line += 1
line += 1

for i in range(max(y) + 1):
    l = []
    for j in range(max(x) + 1):
        l.append('.')
    dots.append(l)

for i in range(len(x)):
    dots[y[i]][x[i]] = '#'

for i in range(line, len(lines)):
    a, b = lines[i].strip().split('=')
    a = a[-1]
    if a == 'x':
        foldX(dots, int(b))
    if a == 'y':
        foldY(dots, int(b))

    print('After step', i - line + 1, ':', countDots(dots))
printDots(dots)
