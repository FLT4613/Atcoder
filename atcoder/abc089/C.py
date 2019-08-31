from collections import Counter
from itertools import combinations


n = int(input())
s = Counter([input()[0] for _ in range(n)])

choices = combinations([x for x in s.keys() if x[0] in 'MARCH'], 3)

if not choices:
    print(0)
    exit()

ans = 0
for choice in choices:
    tmp = 1
    for key in choice:
        tmp *= s[key]
    ans += tmp

print(ans)
