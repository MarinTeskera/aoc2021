f = open('Day08/input.txt', 'r')


def fun(idx, num):
    if len(letters[idx]) == 0:
        for i in num:
            if letters[idx].count(i) == 0:
                letters[idx].append(i)
    else:
        for i in range(len(letters[idx])):
            if num.count(letters[idx][i]) == 0:
                letters[idx][i] = 0
        for i in range(letters[idx].count(0)):
            letters[idx].remove(0)


def decode(line):
    nums, out = line.split(' | ')

    for num in nums.split():
        if len(num) != 5 and len(num) != 6:
            if len(num) == 2:
                fun(2, num)
                fun(5, num)

            if len(num) == 3:
                fun(0, num)
                fun(2, num)
                fun(5, num)

            if len(num) == 4:
                fun(1, num)
                fun(2, num)
                fun(3, num)
                fun(5, num)

            if len(num) == 7:
                fun(0, num)
                fun(1, num)
                fun(2, num)
                fun(3, num)
                fun(4, num)
                fun(5, num)
                fun(6, num)

    for i in range(len(letters)):
        if i != 2 and i != 5:
            letters[i].remove(letters[2][0])
            letters[i].remove(letters[5][1])

    for i in range(2):
        letters[4].remove(letters[1][i])
        letters[6].remove(letters[1][i])

    letters[4].remove(letters[0][0])
    letters[6].remove(letters[0][0])
    rj = ''

    for i in out.split():
        if len(i) == 2:
            rj += '1'
        elif len(i) == 3:
            rj += '7'
        elif len(i) == 4:
            rj += '4'
        elif len(i) == 7:
            rj += '8'
        elif len(i) == 5:
            if i.count(letters[1][0]) + i.count(letters[1][1]) == 1 and i.count(letters[4][0]) + i.count(letters[4][1]) == 2:
                rj += '2'
            if i.count(letters[1][0]) + i.count(letters[1][1]) == 1 and i.count(letters[4][0]) + i.count(letters[4][1]) == 1:
                rj += '3'
            if i.count(letters[1][0]) + i.count(letters[1][1]) == 2 and i.count(letters[4][0]) + i.count(letters[4][1]) == 1:
                rj += '5'
        elif len(i) == 6:
            if i.count(letters[3][0]) == 0 or i.count(letters[3][1]) == 0:
                rj += '0'
            if i.count(letters[2][0]) == 0 or i.count(letters[2][1]) == 0:
                rj += '6'
            if i.count(letters[4][0]) == 0 or i.count(letters[4][1]) == 0:
                rj += '9'

    return int(rj)


lines = f.readlines()
f.close()

signal = ''
out = ''
iValues = []
oValues = []
letters = [[], [], [], [], [], [], []]
rjesenje = 0

for line in lines:
    rjesenje += decode(line)
    letters = [[], [], [], [], [], [], []]

print(rjesenje)
