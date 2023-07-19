def nobelinteger(array):
    array.sort(reverse=True)
    for i in range(len(array)):
        if i==array[i]:
            return 1
    return -1        


array=list(map(int,input().split()))
print(nobelinteger(array))