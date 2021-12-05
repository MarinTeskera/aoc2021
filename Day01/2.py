f = open('input.txt', 'r')
sums = []
larger = 0

elements = f.readlines()

for i in range(len(elements) - 2):
    sums.append(int(elements[i]) + int(elements[i + 1]) + int(elements[i + 2]))
    if (i != 0):
        if (sums[i-1] < sums[i]):
            larger += 1

print (larger)
