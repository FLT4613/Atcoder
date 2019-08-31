s = input()
t = input()
res = []

for s_index in range(len(s)-len(t)+1):
    if s[s_index] in ['?', t[0]]:
        s_p = s[s_index:s_index+len(t)]
        if all(s_p[x] in ['?', t[x]] for x in range(len(s_p))):
            res.append(s[:s_index].replace('?', 'a') + t + s[s_index+len(t):].replace('?', 'a'))
if res:
    print(sorted(res)[0])
else:
    print('UNRESTORABLE')
