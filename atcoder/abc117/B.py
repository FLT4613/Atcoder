n = int(input())
l = [int(x) for x in input().split(' ')]

print('Yes' if max(l) < sum(sorted(l, reverse=True)[1:]) else 'No')
