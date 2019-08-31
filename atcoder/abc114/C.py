n = int(input())

a = []


def func(s):
    if s:
        a.append(int(s))
    if len(s) == len(str(n)):
        return
    func(s + '3')
    func(s + '5')
    func(s + '7')


func('')

print(len([x for x in a if x <= n and len(set(str(x))) == 3]))
