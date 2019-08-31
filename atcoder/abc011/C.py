n = int(input())
ng = sorted([int(input()), int(input()), int(input())], reverse=True)

count=100

if n in ng:
    print('NO')
    exit()

while n>0:
    if count==0:
        print('NO')
        exit()
    elif n-3 not in ng:
        n -= 3
    elif n-2 not in ng:
        n -= 2
    elif n-1 not in ng:
        n -= 1
    else:
        print('NO')
        exit()
    count-=1
    
print('YES')