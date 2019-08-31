s = input()
k = int(input()) - 1

c = 0
for x in s:
    if x != '1':
        break
    c += 1

if c > k:
    print(1)
else:
    print(s[c])
