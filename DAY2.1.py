def rotate_kTimes(arr,k):
    n = len(arr)
    k = k % n

    temp = [0]*n
    read = n-k
    write = 0

    while write <n:
        temp[write]=arr[read]

        read+=1
        write +=1

        if read ==n:
            read =0

    return temp

arr=[1,2,3,4,5,6,7]
print(rotate_kTimes(arr,3))