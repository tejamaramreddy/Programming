def lapindromes(str):
  length = len(str)
  mid = length // 2
  if(length % 2 == 0):
    start = str[:mid]
    end = str[mid:]
  else:
    start = str[:mid]
    end = str[mid+1:]
  F = ""
  F1 = ""
  lstf = []
  lstf1 = []
  for i in start:
    lstf.append(i)
  for i in end:
    lstf1.append(i)
  lstf.sort()
  lstf1.sort()
  for i in lstf:
    F +=i
  for i in lstf1:
    F1 += i
  if(F == F1):
    print("Yes")
  else:
    print("No")
str = "rotor"
lapindromes(str)
