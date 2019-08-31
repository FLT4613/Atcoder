a, b, c = [int(x) for x in input().split(' ')]

if b >= c:
    print(b+c)
else:
    if a >= c-b:
        print(b+c)
    else:
        print(b*2+a+1)
