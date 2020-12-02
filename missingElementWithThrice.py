def MissingElement(arr):
    if(len(arr) == 0):
        return "Null"
    set1 = set(arr)
    setSum = 0
    arrSum = 0

    for i in set1:
        setSum += i
    setSum = setSum * 3
    for i in arr:
        arrSum += i
    Diff = setSum - arrSum
    return Diff // 2


arr = [5, 5, 4, 8, 4, 5, 8, 9, 4, 8 ]

print(MissingElement(arr))
arr=[3,3,3,5]
print(MissingElement(arr))