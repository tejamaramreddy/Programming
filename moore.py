def majorElement(Arr):
    if (len(Arr) == 1 or len(Arr) == 0):
        return -1
    else:
        counter = 0
        maj_element = 0
        for i in range(len(Arr)):
            if counter == 0:
                counter = 1
                maj_element = Arr[i]
            elif maj_element == Arr[i]:
                counter += 1
            else:
                counter -= 1
    return maj_element

def checker(Arr,maj_element):
    counter = 0
    for i in Arr:
        if i == maj_element:
            counter += 1
    if counter >= len(Arr)//2:
        return True
    else:
        return False

Arr = [3,1,3,3,2]

maj_element = majorElement(Arr)
if(checker(Arr,maj_element)):
    print(maj_element)
else:
    print(-1)