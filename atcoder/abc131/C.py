from fractions import gcd
a, b, c, d = [int(x) for x in input().split(' ')]

num = b-a+1
e = b//c - (a-1)//c 
f = b//d - (a-1)//d
g = c*d//gcd(c, d)
print(num - e - f + b//g - (a-1)//g)
