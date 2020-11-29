# Below code works fine only if list have positive numbers
# No duplicate elements 
# And has only one set of numbers which equals to sum
def sumOfTwoNumbers(lst,sumOfTwo):
    if len(lst) <= 0:
        return 0
    else:
        for element in lst:
            difference = abs(sumOfTwo - element)
            if difference in lst[:lst.index(element)] or difference in lst[lst.index(element)+1:]:
                return lst.index(element), lst.index(difference)
lst =   [1,3,7,9,2]
sumOfTwoNumbers(lst,11)
    