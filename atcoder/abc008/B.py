from collections import Counter

n = int(input())
s = Counter([input() for _ in range(0, n)])

print(s.most_common(1)[0][0])