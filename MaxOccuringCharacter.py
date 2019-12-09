
def MaxOccuringCharacter(String):
  lst = []
  output= []
  for i in String:
    if i != ' ':
      lst.append(i)
  for i in lst:
    output.append(lst.count(i))
  if(max(output) == 1):
    print("Every Character occured at single time")
  else:
    print(lst[output.index(max(output))])
  # print(output)

MaxOccuringCharacter('Buffer')


