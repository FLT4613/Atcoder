n = int(input())

a = [0, 0, 1]

if n<4:
    print(a[n-1])
else:
    for i in range(3, n):
        a.append((a[i-1]+a[i-2]+a[i-3])%10007)
    print(a[-1])