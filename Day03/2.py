f = open('Day03/input.txt')

oxy = []
co2 = []

lines = f.readlines()

zeros = 0
ones = 0
more = 0

for line in lines:
    if (line[0] == '1'):
        ones += 1
    else:
        zeros += 1

if (ones > zeros):
    more = 1
elif (ones == zeros):
    more = 2

for line in lines:
    if (more == 1):
        if (line[0] == '1'):
            oxy.append(line)
        if (line[0] == '0'):
            co2.append(line)

    elif (more == 2):
        oxy.append(line)
        co2.append(line)

    else:
        if (line[0] == '0'):
            oxy.append(line)
        if (line[0] == '1'):
            co2.append(line)

for i in range(1, 12):
    oxy_zeros = 0
    co2_zeros = 0
    oxy_ones = 0
    co2_ones = 0

    new_oxy = []
    new_co2 = []

    for line in oxy:
        if (line[i] == '1'):
            oxy_ones += 1
        if (line[i] == '0'):
            oxy_zeros += 1

    for line in co2:
        if (line[i] == '1'):
            co2_ones += 1
        if (line[i] == '0'):
            co2_zeros += 1

    if (oxy_ones >= oxy_zeros):
        for line in oxy:
            if (line[i] == '1'):
                new_oxy.append(line)
    elif (oxy_ones < oxy_zeros):
        for line in oxy:
            if (line[i] == '0'):
                new_oxy.append(line)

    print('oxy_ones:', oxy_ones, 'oxy_zeros:', oxy_zeros)
    print('co2_ones:', co2_ones, 'co2_zeros:', co2_zeros, '\n')

    if (co2_ones >= co2_zeros):
        for line in co2:
            if (line[i] == '0'):
                new_co2.append(line)
    elif (co2_ones < co2_zeros):
        for line in co2:
            if (line[i] == '1'):
                new_co2.append(line)

    if (len(oxy) > 1):
        oxy = new_oxy

    if (len(co2) > 1):
        co2 = new_co2

print(oxy)
print(co2)

print(int(oxy[0], 2) * int(co2[0], 2))
