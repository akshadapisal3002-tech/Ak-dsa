class Solution():
    def Min_Max(self,arr):
       n = len(arr)

       maximum = arr[0]
       minimun = arr[0]

       for i in range(len(arr)):
            if arr[i] > maximum:
               maximum= arr[i]
            if arr[i]< minimun:
               minimun= arr[i]

sol =Solution()
print(sol.Min_Max[1,2,3,4,5,6,])