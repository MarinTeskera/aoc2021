f = open('Day10/input.txt', 'r')

lines = f.readlines()

errrScore = 0
autocorrectScores = []

for i in lines:
    lastOpened = []
    valid = True
    for j in i:
        if j == "(":
            lastOpened.append("(")
        if j == ")":
            if lastOpened[-1] == "(":
                lastOpened.pop(-1)
            else:
                errrScore += 3
                valid = False
                break
        if j == "[":
            lastOpened.append("[")
        if j == "]":
            if lastOpened[-1] == "[":
                lastOpened.pop(-1)
            else:
                errrScore += 57
                valid = False
                break
        if j == "{":
            lastOpened.append("{")
        if j == "}":
            if lastOpened[-1] == "{":
                lastOpened.pop(-1)
            else:
                errrScore += 1197
                valid = False
                break
        if j == "<":
            lastOpened.append("<")
        if j == ">":
            if lastOpened[-1] == "<":
                lastOpened.pop(-1)
            else:
                errrScore += 25137
                valid = False
                break
    if valid:
        autocorrectScore = 0
        while len(lastOpened) > 0:
            autocorrectScore *= 5
            a = lastOpened.pop(-1)
            if a == "(":
                autocorrectScore += 1
            if a == "[":
                autocorrectScore += 2
            if a == "{":
                autocorrectScore += 3
            if a == "<":
                autocorrectScore += 4
        autocorrectScores.append(autocorrectScore)

autocorrectScores.sort()
l = len(autocorrectScores) // 2
print("Error score:", errrScore)
print("Autocorrect score:", autocorrectScores[l])
