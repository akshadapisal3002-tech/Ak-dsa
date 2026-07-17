def rightZero(arr):
    n=len(arr)
    zero = 0 

    for i in range(n):
        if arr[i]!=0:
            arr[zero],arr[i]= arr[i],arr[zero]
            zero+=1

    return arr

arr= [0,1,0,3,12]
print(rightZero(arr))