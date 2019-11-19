def substring(num):
  count = 0
  n = len(num)
  for i in range(n):
    for j in range(i,n):
      if(num[i] == '1' and num[j]== '1'):
        count +=1

  print(count)

substring("10001")
