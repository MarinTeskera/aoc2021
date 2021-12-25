for i in range(2):
    apply(picture, alg)

cnt = 0
for i in picture:
    cnt += i.count('#')