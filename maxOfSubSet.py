arr = [9,6,11,8,10,5,14,13,93,14]
k = 4
def maxOfsubset(arr,k):
    if len(arr) == 1:
        return
    else:
        for i in range(0,len(arr)+1-k):
            print(max(arr[i:i+k]))

print(maxOfsubset(arr,k))