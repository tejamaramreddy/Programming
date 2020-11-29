def sumOfTwo(lst,target):
    pos = -1
    for i in lst:
        pos = pos + 1
        diff = abs(i - target)
        lst[lst.index(i)] = -1
        if len(lst) <= 0:
            return 0
        if diff in lst:
            return pos, lst.index(diff)


nums = [1,3,7,9,2]
target = 11
print(sumOfTwo(nums,target))
nums = [2,7,11,15]
target = 9
print(sumOfTwo(nums,target))
nums = [3,2,4]
target = 6
print(sumOfTwo(nums,target))
nums = [3,3]
target = 6
result = sumOfTwo(nums,target)
print(result)
num = []
target = 9
print(sumOfTwo(nums,target))
nums = [1,2,2,4]
target = 4
print(sumOfTwo(nums,target))




