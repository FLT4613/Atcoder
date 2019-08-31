n = int(input())

a = 0
ans = len(str(n))

while a*a <= n:
    a += 1
    if n % a != 0:
        continue
    b = int(n/a)
    cur = max(len(str(a)), len(str(b)))
    ans = min(ans, cur)

print(ans)
