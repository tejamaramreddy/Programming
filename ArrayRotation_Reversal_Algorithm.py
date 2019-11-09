def arrayRotation(arr):
  start = 0
  end = len(arr)-1
  while(start<end):
    arr[start],arr[end] = arr[end],arr[start]
    start += start
    end -= end

  

arr = [1, 2, 3, 4, 5, 6, 7]
#arrayRotation(arr)
arrayRotation(arr[:2])
arrayRotation(arr[2:])
arrayRotation(arr)

print(arr)
