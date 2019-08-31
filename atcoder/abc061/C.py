n, k = [int(x) for x in input().split(' ')]
ab = sorted([[int(x) for x in input().split(' ')] for _ in range(n)])
index = 0

for a in ab:
    index += int(a[1])
    if index >= k:
        print(a[0])
        break
