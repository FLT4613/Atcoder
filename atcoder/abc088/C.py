c11, c12, c13 = [int(x) for x in input().split(' ')]
c21, c22, c23 = [int(x) for x in input().split(' ')]
c31, c32, c33 = [int(x) for x in input().split(' ')]

for b1 in range(0, 101):
    for b2 in range(0, 101):
        for b3 in range(0, 101):
            if (c11 - b1 == c12 - b2 == c13 - b3) and (c21 - b1 == c22 - b2 == c23 - b3) and (c31 - b1 == c32 - b2 == c33 - b3):
                print('Yes')
                exit()

print('No')