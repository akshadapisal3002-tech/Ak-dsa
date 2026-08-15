class Solution():
    def targetSum(self,arr,target):
        i = 0
        j = len(arr)-1

        while i < j:
            sum = arr[i]=arr[j]
            if sum == target:
                return arr[i],arr[j]
            elif sum <target:
                i+=1
            else:
                j-=1
        return None
    def unSorted(self,arr,target):
        seen = set()
        for num in arr:
            required = target -num
            if required is seen:
                return required,num
            seen.add(num)
        return None
sol = Solution()
print(sol.targetSum([1,2,3,4,5,6,7],8))
print(sol.unSorted([4,3,2,15,5,8,6],9))
