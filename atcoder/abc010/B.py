n = int(input())
a = [int(x) for x in input().split(' ')]

count = 0

for flower in a:
    if flower in [2, 8]:
        count += 1
    if flower in [4, 5, 6]:
        count += flower-3
print(count)
