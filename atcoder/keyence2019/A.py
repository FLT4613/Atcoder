from itertools import permutations

n = ''.join(input().split(' '))

if ('1', '9', '7', '4') in permutations(n):
    print('YES')
else:
    print('NO')
