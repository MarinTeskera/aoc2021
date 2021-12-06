f = open('Day06/input.txt', 'r')

line = f.readline().split(',')

f.close()

d = {0: line.count('0'), 1: line.count('1'), 2: line.count('2'), 3: line.count('3'), 4: line.count(
    '4'), 5: line.count('5'), 6: line.count('6'), 7: line.count('7'), 8: line.count('8')}

for i in range(256):
    nula = d[0]
    for i in range(8):
        d[i] = d[i + 1]
    d[8] = nula
    d[6] += nula

rj = 0
for i in range(9):
    rj += d[i]
print(rj)
