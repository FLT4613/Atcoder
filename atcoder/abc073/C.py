from collections import Counter

n = int(input())
a = Counter([input() for _ in range(n)])

print(len([True for x in a.values() if (x % 2) == 1]))
