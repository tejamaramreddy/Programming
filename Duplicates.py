
def Duplicate(String):
  lst = []
  output= []
  unique = set()
  for i in String.lower():
    if i != ' ':
      lst.append(i)
  for i in lst:
    output.append(lst.count(i))
  if(max(output) == 1):
    print("Every Character occured at single time")
  else:
    for i in output:
      if i > 1:
        unique.add(lst[output.index(i)])
    print(unique)
    # print(lst[output.index(max(output))])
  # print(output)

Duplicate('Python pandas anacondas')


