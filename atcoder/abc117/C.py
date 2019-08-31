n, m = [int(x) for x in input().split(' ')]
x = sorted([int(x) for x in input().split(' ')])

if n >= m:
    print(0)
    exit()

diff = sorted([abs(x[i] - x[i-1]) for i in range(1, m)])
for i in range(n-1):
    diff.pop()

print(sum(diff))
