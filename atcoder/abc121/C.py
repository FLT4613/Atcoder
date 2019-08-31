n, m = [int(x) for x in input().split(' ')]
ab = sorted([[int(x) for x in input().split(' ')]
             for _ in range(int(n))], key=lambda x: x[0])
res = 0
num = 0
for a, b in ab:
    if num + b >= m:
        print(res + a * (m - num))
        exit()
    else:
        res += a * b
        num += b
