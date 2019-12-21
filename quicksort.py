def quicksort(arr,start,end):
  if start < end:
    partitionIndex = partition(arr,start,end)
    quicksort(arr,start,partitionIndex-1)
    quicksort(arr,partitionIndex+1,end)
  return arr
def partition(arr,start,end):
  pivot = arr[end]
  partitionIndex = start
  for i in range(start,end):
    if arr[i] <= pivot:
      arr[i],arr[partitionIndex] = arr[partitionIndex], arr[i]
      partitionIndex = partitionIndex + 1
  arr[partitionIndex],arr[end] = arr[end] , arr[partitionIndex]
  return partitionIndex

arr = [2,4,3,1,5,6,7]
start = 0
end = len(arr)-1
quicksort(arr,start,end)
