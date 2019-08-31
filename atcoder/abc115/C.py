n, k = [int(x) for x in input().split(' ')]
h = sorted([int(input()) for x in range(n)])
print(min([h[i+k-1] - h[i] for i in range(len(h)-k+1)]))
