n = int(input())
a = [int(input()) for x in range(n)]
b = sorted(a[::])
a_1, a_2 = b[-1], b[-2]
c = a.count(a_1)

for i in a:
    if c == 1 and i == a_1:
        print(a_2)
    else:
        print(a_1)
