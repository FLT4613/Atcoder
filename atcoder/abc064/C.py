input()
rates = [int(x) for x in input().split(' ')]

colors = set()

for rate in rates:
    if rate in range(1, 400):
        colors.add('gray')
    elif rate in range(800):
        colors.add('brown')
    elif rate in range(1200):
        colors.add('green')
    elif rate in range(1600):
        colors.add('lightblue')
    elif rate in range(2000):
        colors.add('blue')
    elif rate in range(2400):
        colors.add('yellow')
    elif rate in range(2800):
        colors.add('orange')
    elif rate in range(3200):
        colors.add('red')

print(max(len(colors), 1), len(colors) + len([x for x in rates if x >= 3200]))
