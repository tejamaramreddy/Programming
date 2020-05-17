def arraypair(lst, total):
    result = []
    for i in lst:
        remain = total - i
        if remain in lst[0:lst.index(i)] and lst[lst.index(i):len(lst)]:
            print('(',i,remain,')')
    




arraypair([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)