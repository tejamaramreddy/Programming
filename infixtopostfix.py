
def infixtopostfix(input):
  stack =[]
  output=''
  for i in input:
    if i not in OPERATORS:
      output+= i
    elif i == '(':
      stack.append('(')
    elif i == ')':
      while stack and stack[-1] != '(':
        output+=stack.pop()
      stack.pop()
    else:
      while stack and stack[-1] != '(' and PRIORITY[i] <= PRIORITY[stack[-1]]:
        output+=stack.pop()
      stack.append(i)

  while stack:
    output+=stack.pop()

  print(output)

infixtopostfix("1 * ( 2 + 3 ) / 4")
