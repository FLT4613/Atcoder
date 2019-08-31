w, h, x, y = [float(x) for x in input().split(' ')]
print('{:.10f}'.format(w*h/2.0), 1 if (2*x == w and 2*y == h) else 0)
