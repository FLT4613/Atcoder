from itertools import takewhile
deg, dis = [int(x) for x in input().split(' ')]

directions = ['NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']

# 風程の境界値を取得
# 有効桁数の境界値にする(+0.05)
# 単位を「一分間の風程」に寄せる(*60)
beaufort_scale_boundary = [
    round((x+0.05)*60) for x in [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]
]

# 与えられた風程を、風力0の風程の境界値から比較していく
# 境界値以上の値をx個発見したとき、風力xである
w = len([x for x in takewhile(lambda y: dis>=y, beaufort_scale_boundary)])

if w == 0:
    dir = 'C'
else:
    dir = 'N'
    # 22.5度ずつ、時計回りに判定
    for index, direction in enumerate(directions):
        if 1125+(2250*index) <= deg*10 < 1125+(2250*(index+1)):
            dir = directions[index]
            break
    
print(dir, w)


