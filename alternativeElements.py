def alternativeElements(arr):
    length = len(arr)
    i = 0
    if length == 0 or length == 1:
        for i in arr:
            print(i)
        return
    while(i<length):
        print(arr[i])
        i +=2


arr = [1,2,3,4,5]
alternativeElements(arr)
arr = [1]
alternativeElements(arr)
arr = []
alternativeElements(arr)
arr = [1, 2, 3, 4]
alternativeElements(arr)