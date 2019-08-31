n = input()
a = sorted([int(x) for x in input().split(' ')])
d = int(len(a)/2)

print(len(range(a[d-1], a[d])))
