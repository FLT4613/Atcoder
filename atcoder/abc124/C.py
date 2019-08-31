s = input()

ev = s[0::2]
od = s[1::2]

print(min(ev.count('1')+od.count('0'), ev.count('0')+od.count('1')))
