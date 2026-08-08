class Solution ():
    def Move0and1(self,arr):
        i = 0
        j= len(arr)-1

        while i < j:
            if arr[i] ==0:
                arr[i],arr[j]=arr[j],arr[i]
                j-=1
            else:
                i+=1
        return arr

sol = Solution()
print(sol.Move0and1([1,2,3,4,0,0,0,0,44]))