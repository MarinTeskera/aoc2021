f = open('Day14/input.txt', 'r')


def step(template, d):
    toInsert = []

    for i in range(len(template) - 1):
        a = template[i] + template[i + 1]
        toInsert.append(d[a])

    for i in range(len(toInsert)):
        template.insert(2 * i + 1, toInsert[i])


template = [i for i in f.readline().strip()]
f.readline()
lines = f.readlines()

d = {}

for i in lines:
    a, b = i.strip().split(' -> ')
    d[a] = b

for i in range(10):
    step(template, d)

max = 0
min = len(template)

for i in set(template):
    if template.count(i) > max:
        max = template.count(i)
    if template.count(i) < min:
        min = template.count(i)

print('Part 1:', max - min)
