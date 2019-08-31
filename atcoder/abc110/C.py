from collections import defaultdict

s, t = [s for s in [input(), input()]]


def check(s, t):
    d = defaultdict(set)
    for i in range(len(s)):
        d[s[i]].add(t[i])
    for v in d.values():
        if len(v) > 1:
            return False
    return True


print('Yes' if check(s, t) and check(t, s) else 'No')
