for i in positions:
    pom = abs(positions - i)
    fuel = 0

    for j in pom:
        z = zbroj(j)
        fuel += z

    if minFuel == 0 or fuel < minFuel:
        minFuel = fuel