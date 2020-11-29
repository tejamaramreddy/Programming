def arrayRotation(arr,d):
    if len(arr) <= d:
        d = len(arr) % d
    if d == 0:
        return arr
    temp = [0]*len(arr)
    j = 0
    for i in range(d,len(arr)):
        temp[j] = arr[i]
        j = j + 1

    for i in range(d):
        temp[j] = arr[i]
        j = j + 1
         
    print(temp)


arr = [1,2,3,4,5,6]
d = 3

arrayRotation(arr,d)
        
