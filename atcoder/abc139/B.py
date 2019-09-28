a, b = [int(x) for x in input().split(' ')]

c = 1
d = a - 1
if b == 1:
    print(0)
    exit()

while a < b:
    a += d
    c += 1

print(c)
