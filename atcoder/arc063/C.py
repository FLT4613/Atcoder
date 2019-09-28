uniq = []

for c in input():
    if not uniq:
        uniq += c
    elif uniq[-1] != c:
        uniq += c

print(len(uniq)-1)
