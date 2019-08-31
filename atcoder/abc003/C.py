n, k = [int(x) for x in input().split(' ')]
r = sorted([int(x) for x in input().split(' ')])[-k:]

max_rate = 0
for rate in r:
    max_rate = (max_rate+rate)/2

print('{:.7f}'.format(max_rate))