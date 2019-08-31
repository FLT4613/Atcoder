ax, ay, bx, by, cx, cy = [int(x) for x in input().split(' ')]

# 公式を適用するため、a(0,0)になるよう、b(x,y), c(x,y)を移動
bx -= ax
cx -= ax
by -= ay
cy -= ay

print(abs(bx*cy-cx*by)/2)