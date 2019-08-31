from collections import Counter

s = input()
res = Counter(s)
print(min(res['0'], res['1']) * 2)
