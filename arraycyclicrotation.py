def rotate(arr,start,end):
    while(start < end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
arr = [1]
d = 1
def Cycle(arr,d):
    if len(arr) == 0 or len(arr) == 1:
        print(arr)
        return
    rotate(arr,0,len(arr)-1)
    rotate(arr,0,d - 1)
    rotate(arr,d,len(arr)-1)
    print(arr)
Cycle(arr,d)