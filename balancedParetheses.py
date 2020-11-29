def balanceParathesis(st):
    stack = []
    for i in st:
        if i in '([{':
            stack.append(i)
        else:
            top = stack[-1]
            if top == '(' and i == ')':
                stack.pop()
            elif top == '[' and i == ']':
                stack.pop()
            elif top == '{' and i == '}':
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


print(balanceParathesis('{({([][])}())}'))
{{([][])}()}
