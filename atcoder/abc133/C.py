l, r = [int(x) for x in input().split(' ')]

if (r-l) > 2019:
    print(0)
else:
    a = [x for x in range(l, r+1)]
    res = [i*j % 2019 for i in a for j in a if i != j]
    print(min(res))
