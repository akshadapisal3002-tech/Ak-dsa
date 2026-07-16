def reverse_arr(arr):
    i = 0
    j = len(arr)-1
    while i <= j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr 
arr =[6,4,3,2,5,1]
print(reverse_arr(arr))