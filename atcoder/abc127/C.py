n, m = [int(x) for x in input().split(' ')]
lr = [(int(l), int(r)) for l, r in [input().split(' ') for _ in range(m)]]

l = max([x[0] for x in lr])
r = min([x[1] for x in lr])

print(r-l+1 if l <= r else 0)
