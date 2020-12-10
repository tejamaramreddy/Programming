# def squareroot(n):
#     r = n
#     precision = 10 ** -10
#     while(abs(n -r*r) > precision):
#         r = (r + n/r)/2
#     return round(r)

def squareroot(n):
    low = 0
    high = n
    ans = 0
    while(low <= high):
        mid = (low+high) // 2
        if mid*mid == n:
            return mid
        elif(mid * mid < n):
            low = mid + 1
            
        else:
            high = mid - 1 
    return ans
print(squareroot(4))
print(squareroot(9))
print(squareroot(16))
print(squareroot(25))
print(squareroot(36))
print(squareroot(49))
print(squareroot(64))
