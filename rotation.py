def arrayReverse(arr,start,end):
    while(start < end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

def leftrotate(arr,d):
    if d == 0:
        return arr
    elif d == len(arr):
        return arr
    if d > len(arr):
        d = d % len(arr)
    arrayReverse(arr,0,len(arr)-1)
    arrayReverse(arr,0,d-1)
    arrayReverse(arr,d,len(arr)-1)


arr = [1, 2, 3, 4, 5, 6, 7]  
d = 2
  
leftrotate(arr, d)
print(arr)
