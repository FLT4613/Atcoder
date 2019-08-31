v = int(input())

if v < 100:
  print('00')
elif 100 <= v <= 5000:
  print((str(int(v/100)).zfill(2)))
elif 6000 <= v <= 30000:
  print((str(int(v/1000)+50)))
elif 35000 <= v <= 70000:
  print((str(int(((v/1000)-30)/5)+80)))
elif 70000 < v:
  print('89')