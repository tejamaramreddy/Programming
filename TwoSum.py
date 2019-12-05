def TwoSum(input,result):
  output = ()
  for i in input:
    diff = result - i
    if diff in input[input.index(i):]:
      print(input.index(i),":",input.index(diff))
      

input = [2,7,6,15,3]
result = 9
TwoSum(input,result)
