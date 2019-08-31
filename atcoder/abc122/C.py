n, q = [int(x) for x in input().split(' ')]
s = input()
lr = [[int(x) for x in input().split(' ')] for _ in range(q)]


indexes = [0] * n

for i in range(1, len(s)):
    if s[i-1] == 'A' and s[i] == 'C':
        indexes[i] = indexes[i-1]+1
    else:
        indexes[i] = indexes[i-1]

for l, r in lr:
    print(indexes[r-1]-indexes[l-1])
