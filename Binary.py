def binary(N):
  lst = []
  str1 = ''
  while N > 0:
    lst.append(N%2)
    N = N//2
  print(lst)
  while len(lst) != 0:
    str1 +=str(lst.pop())
  print(str1)
N = pow(2,3)
for i in range(N):
  binary(i)
