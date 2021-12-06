def numberOfFish(list, n):
    print(n)
    if n == 0:
        print(len(list))
        return

    for i in range(len(list)):
        if list[i] == 0:
            list[i] = 6
            list.append(8)
        else:
            list[i] -= 1

    numberOfFish(fish, n - 1)


f = open('Day06/input.txt', 'r')

fish = []

for i in f.readline().split(','):
    fish.append(int(i))

f.close()

print(numberOfFish(fish, 256))
