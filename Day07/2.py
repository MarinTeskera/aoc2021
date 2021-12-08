import numpy as np
import math


f = open('Day07/input.txt', 'r')
line = f.readline()
f.close()

pos = []

for i in line.split(','):
    pos.append(int(i))

pos.sort()

minFuel = 0

sredina = math.floor(sum(pos) / len(pos))

for p in pos:
    for i in range(abs(sredina - p)):
        minFuel += i + 1

print(minFuel)
