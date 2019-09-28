n, x = [int(x) for x in input().split(' ')]
a = [int(x) for x in input().split(' ')] + [0]

c = 0
for i in range(1, len(a)):
    if a[i-1] + a[i] > x:
        tmp = a[i]
        a[i] = x - a[i-1]
        c += tmp - a[i]

for i in range(1, len(a))[::-1]:
    if a[i-1] + a[i] > x:
        tmp = a[i]
        a[i] = x - a[i-1]
        c += tmp - a[i]

print(c)
