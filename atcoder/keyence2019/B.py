s = input()

keyence = 'keyence'

for index, char in enumerate(s):
    if char!=keyence[0]:
        break
    keyence = keyence[1:]

keyence = keyence[::-1]
for index, char in enumerate(s[::-1]):
    if keyence and char!=keyence[0]:
        break
    keyence = keyence[1:]
    
if not keyence:
    print('YES')
else:
    print('NO')

