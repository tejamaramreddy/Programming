def secondLargest(arr):
    largest = arr[0]
    slargest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
        elif i > slargest:
            slargest = i
    print(slargest)

arr = [3, 2, 1, 56, 10000, 167]
secondLargest(arr)