f = open('Day01/input.txt', 'r')
larger = 0

elements = f.readlines()

for i in range(1, len(elements)):
    if (int(elements[i-1]) < int(elements[i])):
        larger += 1


print("Larger: ", larger)

