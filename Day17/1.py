def check(xFirst, yFirst, x, y, xMin, xMax, yMin, yMax, tmpX, tmpY, possible):
    if (tmpX >= xMin and tmpX <= xMax) and (tmpY >= yMin and tmpY <= yMax) and possible.count((xFirst, yFirst)) == 0:
        possible.append((xFirst, yFirst))
    if tmpX > xMax or tmpY < yMin:
        return

    tmpX += x
    tmpY += y

    if x > 0:
        x -= 1
    y -= 1

    check(xFirst, yFirst, x, y, xMin, xMax, yMin, yMax, tmpX, tmpY, possible)


xMin = 32
xMax = 65

yMin = -225
yMax = -177

possible = []

for i in range(xMax + 1):
    for j in range(yMin, 225):
        check(i, j, i, j, xMin, xMax, yMin, yMax, 0, 0, possible)

print(len(possible))
