def stockspan(arr):
  result = []
  result.append(1)
  for i in range(1,len(arr)):
    count = 1
    j = i-1
    while arr[i] >= arr[j]  and j>=0:
      count+=1
      j-=1
    result.append(count)

  print(result)



arr = [100, 80, 60, 70, 60, 75, 85]
stockspan(arr)

