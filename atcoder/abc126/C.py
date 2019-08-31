n, k = [int(x) for x in input().split(' ')]

res = 0.0
for dice in range(1, n+1):
    tmp = dice
    cnt = 0
    while k > tmp:
        tmp *= 2
        cnt += 1
    res += (1 / n) * (0.5 ** cnt)

print(res)
