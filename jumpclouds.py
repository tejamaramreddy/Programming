def jumpclouds(arr):
   n = len(arr)
   count, i = 0,0
   while(i< n - 1):
       if(i<n-2 and arr[i+2] == 0):
           i += 1
       if(i != n-1):
           count +=1
       i += 1
   return count



arr = [0, 0, 1, 0, 0, 1, 0]

print(jumpclouds(arr))
arr = [0, 0, 0, 1, 0, 0]

print(jumpclouds(arr))

        