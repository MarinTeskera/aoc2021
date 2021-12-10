f = open('Day09/input.txt', 'r')

l = f.readlines()
risk = 0
lines = []

for i in l:
    list = []
    for j in i:
        if j != '\n':
            list.append(int(j))
    lines.append(list)

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i == 0 and j == 0:
            if lines[i][j] < min(lines[i][j + 1], lines[i + 1][j]):
                risk += int(lines[i][j]) + 1
        elif i == 0 and j == len(lines[0])-1:
            if lines[i][j] < min(lines[i][j - 1], lines[i + 1][j]):
                risk += lines[i][j] + 1
        elif i == len(lines) - 1 and j == 0:
            if lines[i][j] < min(lines[i][j + 1], lines[i - 1][j]):
                risk += lines[i][j]+1
        elif i == len(lines) - 1 and j == len(lines[0])-1:
            if lines[i][j] < min(lines[i][j - 1], lines[i - 1][j]):
                risk += lines[i][j]+1
        elif i == 0:
            if lines[i][j] < min(lines[i][j + 1], lines[i][j - 1], lines[i + 1][j]):
                risk += lines[i][j]+1
        elif i == len(lines) - 1:
            if lines[i][j] < min(lines[i][j + 1], lines[i][j - 1], lines[i - 1][j]):
                risk += lines[i][j]+1
        elif j == 0:
            if lines[i][j] < min(lines[i][j + 1], lines[i + 1][j], lines[i - 1][j]):
                risk += lines[i][j] + 1
        elif j == len(lines[0])-1:
            if lines[i][j] < min(lines[i][j - 1], lines[i + 1][j], lines[i - 1][j]):
                risk += lines[i][j] + 1
        else:
            if lines[i][j] < min(lines[i][j + 1], lines[i][j - 1], lines[i + 1][j], lines[i - 1][j]):
                risk += lines[i][j] + 1

print(risk)
