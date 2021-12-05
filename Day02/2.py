f = open('Day02/input.txt', 'r')
horizontal = 0
aim = 0
depth = 0

lines = f.readlines()

for line in lines:
    a, b = line.split(' ')
    if (a == 'forward'):
        horizontal += int(b)
        depth += aim * int(b)
    elif(a == 'down'):
        aim += int(b)
    else:
        aim -= int(b)

print(horizontal * depth)
