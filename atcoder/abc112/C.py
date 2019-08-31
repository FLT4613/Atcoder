from itertools import product
n = int(input())

pos = [[int(x) for x in input().split(' ')] for _ in range(n)]

for cx, cy in product(range(101), range(101)):
    H = max(max([abs(p[0]-cx)+abs(p[1]-cy)+p[2] for p in pos if p[2] != 0]), 1)
    if all(max(H-abs(p[0]-cx)-abs(p[1]-cy), 0) == p[2] for p in pos):
        print(cx, cy, H)
        exit()
