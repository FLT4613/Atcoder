n = int(input())
h = [int(x) for x in input().split(' ')]

i = 1
lc = []
c = 0

while i < len(h):
    if h[i-1] >= h[i]:
        c += 1
    else:
        lc.append(c)
        c = 0
    i += 1
lc.append(c)
print(max(lc))
