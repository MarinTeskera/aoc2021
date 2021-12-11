f = open('Day11/input.txt', 'r')


def flash(grid, i, j, flashed, flashes):
    if flashed.count((i, j)) != 0:
        return
    if grid[i][j] > 9:
        flashed.append((i, j))
        flashes += 1
        for (i, j) in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if 0 <= i < 10 and 0 <= j < 10:
                grid[i][j] += 1
                if grid[i][j] > 9 and flashed.count((i, j)) == 0:
                    flash(grid, i, j, flashed, flashes)


lines = f.readlines()
f.close()

grid = []
flashes = 0
flashed = []

for line in lines:
    lista = []
    for i in line:
        if i != '\n':
            lista.append(int(i))
    grid.append(lista)

i = 0

while(True):
    flashed = []
    for j in range(len(grid)):
        for k in range(len(grid[j])):
            grid[j][k] += 1
            if grid[j][k] > 9:
                flash(grid, j, k, flashed, flashes)
    for j in range(len(grid)):
        for k in range(len(grid[j])):
            if grid[j][k] > 9:
                grid[j][k] = 0
    flashes += len(flashed)
    i += 1
    if len(flashed) == 100:
        break

print("Step:", i)
