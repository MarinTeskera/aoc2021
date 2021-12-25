f = open('Day12/input.txt', 'r')

count = 0


def findPath(paths, start, used):
    global count
    for i in paths[start]:
        if i == 'end':
            used.append('end')
            count += 1
        if used.count(i) == 0 or i.isupper():
            findPath(paths, i, used + [i])


lines = f.readlines()
paths = {}

for line in lines:
    a, b = line.split('-')
    c = str()

    for i in b:
        if i != '\n':
            c += i

    if not (a in paths.keys()):
        paths[a] = set([])
    if not (c in paths.keys()):
        paths[c] = set([])

    paths[a].add(c)
    paths[c].add(a)

findPath(paths, 'start', ['start'])
print(count)
