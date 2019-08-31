row, col = [int(x) for x in input().split(' ')]
sy, sx = [int(x) for x in input().split(' ')]
gy, gx = [int(x) for x in input().split(' ')]
field = [input() for x in range(0, row)]
queue = [(sy-1, sx-1)]
memo = set([(sy-1, sx-1)])


def get_children(y, x):
    result = []
    if field[y][x+1] == '.' and (y, x+1) not in memo:
        result.append((y, x+1))
    if field[y][x-1] == '.' and (y, x-1) not in memo:
        result.append((y, x-1))
    if field[y+1][x] == '.' and (y+1, x) not in memo:
        result.append((y+1, x))
    if field[y-1][x] == '.' and (y-1, x) not in memo:
        result.append((y-1, x))
    return result


count = 0
while queue and (gy-1, gx-1) not in queue:
    count += 1
    points = queue
    queue = []
    for point in points:
        children = get_children(point[0], point[1])
        memo.update(children)
        queue.extend(children)

print(count)
