import numpy as np

f = open('Day07/input.txt', 'r')
line = f.readline()
f.close()

pos = []
for i in line.split(','):
    pos.append(int(i))
positions = np.array(pos)

print(positions)
minFuel = 0

for i in positions:
    pom = positions - i
    fuel = sum(abs(pom))

    if minFuel == 0 or fuel < minFuel:
        minFuel = fuel

print(minFuel)
