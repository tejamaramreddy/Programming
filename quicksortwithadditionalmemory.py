def sort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    
    return sort(less) + [pivot] + sort(greater)

arr = [2,4,3,1,5,6,7]
sort(arr)
