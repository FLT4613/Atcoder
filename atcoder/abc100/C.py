input()

c = 0
for n in [int(x) for x in input().split(' ') if int(x) % 2 == 0]:
    while n % 2 == 0:
        n /= 2
        c += 1

print(c)
