

def Hashing(arr):
    hash = {}
    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    return hash

def findingNth(hash,n):
    for i in hash.keys():
        if hash[i] == n:
            return i
    return "Not found"
def nMostfrequent(arr,n):
    if(len(arr)>1 and n > 0):
        hash = Hashing(arr)
        print(findingNth(hash,n))
    else:
        return 'Null'

arr = [1,2,2,2,4,4,4,4,5,5,5,5,5,7,7,8,8,8,8]
n = 4
nMostfrequent(arr,n)