"""
Given an array A of positive integers. Your task is to find the leaders in the array. 
An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 
A[] = {16,17,4,3,5,2}
Output: 17 5 2
"""

def Leader(Arr,N):
    output = ''
    for i in range(N):
        temp_Arr = Arr[i:]
        temp_Arr.sort(reverse = True)
        if temp_Arr[0] == Arr[i]:
            output = output + str(Arr[i]) + ' '
    return output

Arr = [16,17,4,3,5,2]
N = len(Arr)
print(Leader(Arr,N)  )   
