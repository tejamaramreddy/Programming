def Missing(array1,array2):
    if len(array1)-1 != len(array2):
        return "Input not valid!"

    sum1 = 0
    sum2 = 0
    for i in array1:
        sum1 += i
    for i in array2:
        sum2 += i

    return abs(sum1-sum2)


array1 = [9, 7, 8, 5, 4, 6, 2, 3, 1]
array2 = [2, 3, 4, 9, 1, 8, 5, 6]
print(Missing(array1,array2))