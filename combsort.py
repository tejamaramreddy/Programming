def Combsort(arr):
    if len(arr) <=1:
        return arr
    else:
        n = len(arr)
        gap = n
        swapped = True
        while gap != 1 or swapped:
            gap = int(gap *10 // 13)
            if gap < 1:
                gap = 1
            swapped = False
            for i in range(0,n-gap):
                if arr[i] > arr[i+gap]:
                    arr[i],arr[i+gap] = arr[i+gap],arr[i]
                    swapped = True
    return arr

array = [50, 10, 25, -45, 30, 28]
print(Combsort(array))


