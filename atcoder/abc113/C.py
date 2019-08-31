from collections import defaultdict

n, m = [int(x) for x in input().split(' ')]
py = [tuple(input().split(' ')) for _ in range(m)]

d = defaultdict(list)

for x, y in py:
    d[x].append(int(y))

ans = {}

for k, v in d.items():
    for i, x in enumerate(sorted(v), start=1):
        ans[(k, str(x))] = k.zfill(6) + str(i).zfill(6)

for x in py:
    print(ans[x])
