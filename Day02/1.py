f = open('Day02/input.txt', 'r')

horizontal = 0
depth = 0

lines = f.readlines()

for line in lines:
    a, b = line.split(' ')
    if (a == 'forward'):
        horizontal += int(b)
    elif (a == 'down'):
        depth += int(b)
    else:
        depth -= int(b)

print(horizontal * depth)
