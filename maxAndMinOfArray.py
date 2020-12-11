def maxandmin(arr):
    max = arr[0]
    min = arr[0]
    if len(arr) == 1:
        print(max,min)
        return
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    print(min,max)

arr = [3, 2, 1, 56, 10000, 167]
maxandmin(arr)
arr = [1, 345, 234, 21, 56789]
maxandmin(arr)
arr = [1]
maxandmin(arr)