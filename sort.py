# any element of array 1 present in array 2 return true else return false
arr1 = [1,2,45,78,45]
arr2 = [2,4,6,876,345,876]
def check(arr1,arr2):
    for i in arr1:
        if i in arr2:
            return True
    return False

print(check(arr1,arr2))
