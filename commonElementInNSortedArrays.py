arr1 =  [[23, 34, 67, 89, 123, 566, 1000],
        [11, 22, 23, 24,33, 37, 185, 566, 987, 1223, 1234],
        [23, 43, 67, 98, 566, 678],
        [1, 4, 5, 23, 34, 76, 87, 132, 566, 665],
        [1, 2, 3, 23, 24, 344, 566]]

def binarySearch(arr,key):
    if len(arr) < 1:
        return arr
    else:
        start = 0
        end = len(arr)
        while(start <= end):
            mid = (start + end) // 2
            if arr[mid] == key:
                return True
            if arr[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
    return False





