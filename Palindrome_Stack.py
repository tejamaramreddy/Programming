def Palindrome_Stack(str):
  lst = []
  stack = []
  temp = []
  for i in str:
    lst.append(i)
  mid = len(lst)//2
  if mid%2 != 0:
    mid -=1
  for j in range(mid):
    stack.append(lst[j])
  for i in range(mid):
    temp.append(stack.pop())
  if temp == lst[mid-1::-1]:
    print("Palindrome")
  print(lst[mid-1::-1])
  print(temp)  

Palindrome_Stack('madam')

  
