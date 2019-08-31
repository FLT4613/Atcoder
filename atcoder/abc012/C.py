t = 2025 - int(input())
ret = []

for i in range(1, 10):
    x = t / i
    if len(str(int(x))) == 1 and str(x).endswith('0'):
        ret.append('{} x {}'.format(i, int(x)))
    if t < i:
        break

print('\n'.join(sorted(ret)))

