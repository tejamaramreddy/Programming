# Given an increasing sequence of numbers from 1 to n with only one missing number, how can you find that missing number without traversing the sequence in linear fashion. In other words, time complexity of your algorithm must be less than O(n)?

# For example, if the given sequence is 1,2,4,5,6,7,8 then the missing number is 3. If the given sequence is 1,3,4,5 then the missing number is 2. For the input 2,3,4,5 output returned should be 1 as it is the missing number.


arr = [1,2,4,5,6,7,8]

def findingMissingElement(arr):
    if len(arr) <2:
        return
    sum = 0
    for item in arr:
        sum += item
    lastdigit = arr[-1]
    sumOfN = (lastdigit*(lastdigit + 1))//2
    print(sumOfN - sum)


findingMissingElement(arr)