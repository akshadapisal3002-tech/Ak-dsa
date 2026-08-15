class Solution():
    def small_large(self,arr):
        samllest = arr[0]
        largest = arr[0]

        i = 0
        while i <len(arr):
            if arr[i]>largest:
                largest = arr[i]
            
            if arr[i] < samllest:
                samllest = arr[i]
            
            i+=1
        return samllest, largest
sol = Solution()
print(sol.small_large([1,2,3,4,5,6,7]))



