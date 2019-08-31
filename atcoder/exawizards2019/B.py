N = int(input())
s = input()

from collections import Counter

s = Counter(s)

if s['R'] > s['B']:
    print('Yes')
else:
    print('No')