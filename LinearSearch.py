def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return arr[i]
    return -1

print(LinearSearch([0,1,2,3,4,5,6,7,8,9],10))
