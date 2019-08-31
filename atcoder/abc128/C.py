n, m = [int(x) for x in input().split(' ')]
s = [[int(x) for x in input().split(' ')[1:]] for _ in range(m)]
p = input().split(' ')

cnt = 0
for i in range(0, 2**n):
    ptn = '0'+format(i, '010b')[::-1]
    light = []
    for j, sw in enumerate(s):
        on_sws = [ptn[sw_i] for sw_i in sw if ptn[sw_i] == '1']
        light.append(len(on_sws) % 2 == int(p[j]))
    if all(light):
        cnt += 1

print(cnt)
