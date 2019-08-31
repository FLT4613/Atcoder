antennas = [int(input()) for _ in range(5)]
k = int(input())
if max(antennas) - min(antennas) > k:
    print(':(')
else:
    print('Yay!')
