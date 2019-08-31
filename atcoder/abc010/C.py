txa, tya, txb, tyb, T, V = [int(x) for x in input().split(' ')]
n = int(input())

speed = T*V
houses = [[int(x) for x in input().split(' ')] for _ in range(n)]

for house in houses:
    to_house = pow(pow(txa-house[0], 2)+pow(tya-house[1], 2), 0.5)
    to_current = pow(pow(txb-house[0], 2)+pow(tyb-house[1], 2), 0.5)
    if speed >= (to_house + to_current):
        print('YES')
        exit()

print('NO')
