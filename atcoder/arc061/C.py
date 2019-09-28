s = input()
l = len(s)

a = []

for i in range(2 ** (l-1)):
    f = []
    b = '{:b}'.format(i).zfill(l-1)
    for j, c in enumerate(s):
        f.append(c)
        if j < l-1 and b[j] == '1':
            f.append('+')
    a.append(eval(''.join(f)))

print(sum(a))
