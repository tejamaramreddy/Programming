def linearsearch(arr , key):
  for i in arr:
    if key == i:
      print(key, " at : ", arr.index(i))

arr = [12,45,21,34,67,90.65]
linearsearch(arr,67)
