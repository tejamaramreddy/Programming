arr = [0, 3, 1, 3, 0]
found  = False
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] == arr[j]:
#             found = True
#             print(arr[i])
#             continue
# if found == False:
#     print(-1)

map = {}
for i in arr:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1

for i in map:
    if map[i] > 1:
        found = True
        print(i)
if found == False:
    print(-1)