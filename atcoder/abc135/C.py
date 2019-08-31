n = int(input())
a = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]
c = 0

for i in range(n):
  if a[i] > 0:
    d = min(a[i], b[i])
    c += d
    a[i] -= d
    b[i] -= d

  if b[i] > 0:
    d = min(a[i+1], b[i])
    c += d
    a[i+1] -= d
    b[i] -= d

print(c)
