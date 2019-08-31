from math import ceil
minutes = [int(input()) for _ in range(5)]

arr = [(x, x % 10) for x in minutes if x % 10 != 0]
if arr:
    x = min(arr, key=lambda x: x[1])
    minutes.remove(x[0])
    print(sum([ceil(x/10)*10 for x in minutes])+x[0])
else:
    print(sum(minutes))
