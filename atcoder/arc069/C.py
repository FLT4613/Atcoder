n, m = [int(x) for x in input().split(' ')]

ans = 0

if m == 1:
    ans = 0
elif n * 2 > m:
    ans = m // 2
elif n * 2 + 4 > m:
    ans = n
else:
    ans = (m - (n*2)) // 4 + n

print(ans)
