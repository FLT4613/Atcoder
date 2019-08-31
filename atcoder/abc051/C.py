sx, sy, tx, ty = [int(x) for x in input().split(' ')]

rap_1 = abs(ty-sy) * ['U'] + abs(tx-sx) * ['R']
rap_1 += abs(ty-sy) * ['D'] + abs(tx-sx) * ['L']
rap_2 = ['L'] + (abs(ty-sy)+1) * ['U'] + (abs(tx-sx)+1) * ['R'] + ['D']
rap_2 += ['R'] + (abs(ty-sy)+1) * ['D'] + (abs(tx-sx)+1) * ['L'] + ['U']

print(''.join(rap_1)+''.join(rap_2))
