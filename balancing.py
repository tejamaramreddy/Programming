def balancing(arr):
  l1 = arr[0]
  l2 = arr[1]
  if l1[0]<l1[1]:
    diff = l1[1] - l1[0]
    if diff in l2:
      return diff
    else:
      for i in l2:
        for j in l2:
          if ((l1[0]+j) == l1[1]+i):
            return f"{i,j}"
  if l1[0]>l1[1]:
    diff = l1[0] - l1[1]
    if diff in l2:
      return diff
    else:
      for i in range(len(l2)):
        for j in range(len(l2)):
          if (l1[0]+l2[i]) == (l1[1]+ l2[j]):
            return f"{l2[i],l2[j]}"

  if l1[0] == l1[1]:
    return 0

         
    

     




print(balancing([[13, 3], [1, 2, 3, 11, 14]]))
