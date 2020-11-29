array = [0, 1, 2, 2, 4, 5, 5, 5, 8]
Num = 5
low = 0
high = len(array) - 1
while(low <= high):
    mid = (low + high) // 2
    if (array[mid] == Num and ((mid == high) or Num < array[mid + 1])):
        print(mid)
        break
    elif array[mid] > Num:
        high = mid - 1
    else:
        low = mid + 1
