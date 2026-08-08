class Solution():
    def Two_sum(self,arr,target):
        i =0
        j= len(arr)-1

        while i < j:
            Total = arr[i]+arr[j]
            if target == Total:
                return arr[i],arr[j]
            elif target > Total:
                i+=1
            else:
                j-=1
        return None

sol = Solution()
print(sol.Two_sum([1,2,3,4,5,6],8))
