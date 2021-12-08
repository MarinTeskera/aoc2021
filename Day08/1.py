f = open('Day08/input.txt', 'r')

lines = f.readlines()
f.close()

signal = ''
out = ''
iValues = []
oValues = []
count = 0

for line in lines:
    signal, out = line.split(' | ')

    iValues.append(signal.split())
    oValues.append(out.split())

    for i in out.split():
        if (len(i) != 5 and len(i) != 6):
            count += 1

print(count)
