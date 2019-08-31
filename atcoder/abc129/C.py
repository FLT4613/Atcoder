n, m = [int(x) for x in input().split(' ')]
a = set(int(input()) for x in range(m))

m = [0] * n
m[0] = 1 if 1 not in a else 0

if n == 1:
    print(m[0])
    exit()

m[1] = 2 if 2 not in a else 0

if m[0] == 0 and m[1] == 2:
    m[1] = 1

for i in range(2, n):
    if i+1 not in a:
        m[i] = m[i-1] + m[i-2]

print(m[-1] % 1000000007)
