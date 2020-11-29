stringInput = input()
alpha = [0]
for i in range(ord('a'),ord('z')+1):
    alpha.append(chr(i))

sum = 0
for i in stringInput:
    sum += alpha.index(i)

print(sum)