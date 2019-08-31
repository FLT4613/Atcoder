from math import ceil

n = int(input())

x = min([int(input()) for _ in range(5)])

print(4 + ceil(n/x))
