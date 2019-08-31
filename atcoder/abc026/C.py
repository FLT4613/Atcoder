n = int(input())

b = [int(input()) for _ in range(n-1)]


res = {}

for i in range(1, 21)[::-1]:
    worker = [ind for ind, x in enumerate(b, start=2) if x == i]
    if worker:
        worker_salary = [res[x] for x in worker]
        res[i] = max(worker_salary) + min(worker_salary) + 1
    else:
        res[i] = 1

print(res[1])
