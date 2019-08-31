n = int(input()) % 30
cards = ['1', '2', '3', '4', '5', '6']
for i in range(0, n):
    cards[i%5], cards[i%5+1] = cards[i%5+1], cards[i%5]

print(''.join(cards))