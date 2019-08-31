from string import ascii_lowercase
s = input()

if s=='a':
  print('-1')
elif len(s)==1:
  index = ascii_lowercase.find(s) - 1
  print(ascii_lowercase[index])
else:
  print(s[:-1])