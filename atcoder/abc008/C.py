n = int(input())
c = [int(input()) for _ in range(n)]

# 期待値
ev = 0.0

for coin in c:
    # 対象のcoinを約数としてカウントしない(-1)
    div_num = len([x for x in c if (coin % x) == 0])-1
    ev += (div_num+2) / (2*div_num+2) if div_num % 2 == 0 else 0.5

print(ev)
