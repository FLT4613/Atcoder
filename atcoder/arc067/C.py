from collections import Counter


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


n = int(input())

t = []
for tmp in range(2, n+1):
    t.extend(prime_decomposition(tmp))

ans = 1

for v in Counter(t).values():
    ans *= v + 1


print(ans % (10**9+7))
