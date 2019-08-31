n, m = [int(x) for x in input().split(' ')]

edges = [(input().split(' ')) for _ in range(m)]
ans = 0


def bfs(bridge):
    queue = ['1']
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        next_nodes = [
            x[1] for x in edges if x[0] == node and x[1] not in visited and bridge != x
        ] + [
            x[0] for x in edges if x[1] == node and x[0] not in visited and bridge != x
        ]
        queue.extend(next_nodes)
        if len(visited) == n:
            return False
    return True


for edge in edges:
    if bfs(edge):
        ans += 1

print(ans)
