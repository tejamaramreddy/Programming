max = 10
def create():
  stack = []
  return stack

def push(stack,ele):
  if len(stack)>=10:
    print("Stack is full")
  else:
    stack.append(ele)

def pop(stack):
  if len(stack) == 0:
    print("Stack is empty")
  else:
    stack.pop()

def display(stack):
  if len(stack) == 0:
    print("No elements in stack")
  else:
    print(stack)

def top(stack):
  print(stack[len(stack)-1])

stack = create()
number_of_elements = int(input("Enter number of elements"))
for i in range(number_of_elements):
  push(stack,input()) 
number_of_elements_pop = int(input("number_of_elements_pop"))
for i in range(number_of_elements_pop):
  pop(stack)
display(stack)
top(stack)
