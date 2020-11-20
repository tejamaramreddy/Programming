def solve (A):
    # Write your code here
    A = list(A)
    mid = len(A) // 2
    firstHalf = A[:mid]
    secondHalf = A[mid:]
    finalNumber = ''
    for i in firstHalf:
        finalNumber = finalNumber +str(i)[:1]
    for i in secondHalf:
        finalNumber = finalNumber + str(i)[-1]
    if int(finalNumber)% 11 == 0:
        return 'OUI'
    else:
        return "NON"
    

N = int(input())
A = map(int, input().split())

out_ = solve(A)
print (out_)