class Solution():
    def RemoveDuplicates(self,arr):
        i =0
        j =1

        while j<len(arr):
            if arr[i] != arr[j]:
                i+=1
                arr[i]=arr[j]
            j+=1
        return arr[:i+1]
sol = Solution()
print(sol.RemoveDuplicates([1,1,2,3,4,4,5,6,6,6,7,]))