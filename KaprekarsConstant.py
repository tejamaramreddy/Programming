def KaprekarsConstant(num):
  lst = []
  asc = []
  des = []
  temp = 0
  temp1 = 0
  diff = 0
  count = 0
  while num>0:
    t = num % 10
    lst.append(t)
    num = num//10
  asc = lst[:]
  des = lst[::-1]
  for i in asc:
    temp = temp*10+i
  for i in des:
    temp1 = temp1*10+i
  if temp1 > temp:
    temp1,temp = temp,temp1
  while diff != 6174:
    diff = temp - temp1
    KaprekarsConstant(diff)
    count = count + 1

  return count



  print("temp:",temp)
  print("temp1:",temp1)

  




print(KaprekarsConstant(int(input())))
