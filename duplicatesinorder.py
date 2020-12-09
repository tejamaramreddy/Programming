arr = [1, 2, 3, 1, 3, 6, 6]
found  = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            found = True
            print(arr[i])
            continue
if found == False:
    print(-1)