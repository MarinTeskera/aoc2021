f = open('Day03/input.txt', 'r')

gamma = 0
epsilon = 0

lines = f.readlines()

for i in range(12):
    ones = 0
    zeros = 0

    for line in lines:
        if (line[i] == '1'):
            ones += 1
        else:
            zeros += 1

    if (ones > zeros):
        gamma = 2 * gamma + 1
        epsilon = 2 * epsilon
    if (zeros > ones):
        gamma = 2 * gamma
        epsilon = 2 * epsilon + 1

print(gamma * epsilon)
