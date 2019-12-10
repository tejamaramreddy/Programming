def palindrome(str):
  stack = []
  output =''
  mid = len(str)//2
  temp = mid
  if len(str) % 2 !=0:
    mid +=1

  for i in range(mid,len(str)):
    stack.append(str[i])
  while len(stack) != 0:
    output += stack.pop()
  if(output == str[:temp]):
    print('Palindrome')
  else:
    print('Not a palindrome')
  
  print(output)
  print(str[:temp])
  print('\n')

palindrome('madam')
palindrome('12344321')
palindrome('aaabcbaaa')
