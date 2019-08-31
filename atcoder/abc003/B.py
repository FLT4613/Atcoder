S, T = input(), input()

replace_chars = 'atcoder'
loser = False

# 敗北条件
for index in range(0, len(S)):
    if S[index] == '@' and T[index] not in replace_chars + '@':
        loser = True
    if T[index] == '@' and S[index] not in replace_chars + '@':
        loser = True
    if S[index] != T[index] and '@' not in [S[index], T[index]]:
        loser = True

if loser:
    print('You will lose')
    exit()

# 負けなきゃ勝ち
print('You can win')
