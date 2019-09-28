from collections import Counter

n = int(input())

s = set()
res = Counter([tuple(sorted(input())) for _ in range(n)])
print(sum((x*(x-1))//2 for x in res.values()))
