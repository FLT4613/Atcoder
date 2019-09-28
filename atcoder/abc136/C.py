n = int(input())
h = [int(x) for x in input().split(' ')]
m = 0
for i in range(0, n):
    m = max(h[i], m)
    if m - h[i] > 1:
        print('No')
        exit()

print('Yes')
