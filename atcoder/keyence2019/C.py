n = int(input())
a = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]

if sum(a) < sum(b):
    print('-1')
    exit()

count = 0
sabun = [a[i]-b[i] for i, _ in enumerate(a)]
husoku = sum([x for x in sabun if x < 0])
sabun.sort(reverse=True)

for i in sabun:
    if husoku >= 0:
        break
    husoku += i
    count += 1

print(len([x for x in sabun if x < 0]) + count)
