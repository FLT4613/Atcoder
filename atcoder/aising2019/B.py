from itertools import permutations

n  = int(input())
a, b = [int(x) for x in input().split(' ')]
p = sorted([int(x) for x in input().split(' ')])

p_easy = len([x for x in p if x<=a])
p_normal = len([x for x in p if a<x<=b])
p_hard = len([x for x in p if b<x])

print(min(p_easy,p_normal,p_hard))