from collections import defaultdict

n = int(input())

m = defaultdict(lambda: 99999)

s = input()
co = set(s)
for c in co:
    m[c] = min(m[c], s.count(c))

for _ in range(1, n):
    s = input()
    co &= set(s)
    for c in co:
        m[c] = min(m[c], s.count(c))

ret = sum([[k]*v for k, v in m.items() if k in co], [])

print(''.join(sorted(ret)))
