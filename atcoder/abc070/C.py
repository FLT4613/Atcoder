from fractions import gcd

n = int(input())
t = sorted([int(input()) for _ in range(n)])

result = t.pop(0)


def lcm(a, b):
    return a*b // gcd(a, b)


for timer in t:
    result = lcm(result, timer)

print(result)
