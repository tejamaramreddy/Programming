def squareroot(n):
    r = n
    precision = 10 ** -10
    while(abs(n -r*r) > precision):
        r = (r + n/r)/2
    return round(r)

print(squareroot(4))
print(squareroot(9))
print(squareroot(16))
print(squareroot(25))