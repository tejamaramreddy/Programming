def binarysearch(arr, key):
  found = False
  bottom = 0
  top = len(arr) - 1
  while bottom <= top and found == False:
    mid = (top + bottom) // 2
    if arr[mid] == key:
      found = True
    elif arr[mid] < key:
      bottom = mid+1
    else:
      top = mid - 1
  return found

arr = [12,13,14,15,16,17,18,19]
binarysearch(arr,15)
