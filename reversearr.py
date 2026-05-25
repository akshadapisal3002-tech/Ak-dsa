def reversearr(arr, low,high):
    if low<= high:
        return
    arr[low],arr[high] = arr[high],arr[low]

    reversearr(arr,low+1,high-1)

arr = list(map(int,input().split()))
reversearr(arr,0,len(arr)-1)
print(arr)

