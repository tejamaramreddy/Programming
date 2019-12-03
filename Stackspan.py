def span(prices):
  stack = [0]
  span = [1]
  for i in range(1,len(prices)):
    while prices[stack[-1]] < prices[i]:
      stack.pop()
    if len(stack) > 0:
      span.append(i-stack[-1])
    else:
      span.append(i+1)
    stack.append(i)
  print(span)

prices =  [100, 27, 14, 21, 30, 22]
span(prices)
