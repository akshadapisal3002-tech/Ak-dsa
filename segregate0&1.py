class Solution:
    def segregate0and1(self, arr):
        i = 0
        j = len(arr)-1
        while i<j:
            if arr[i]==0:
                i+=1
            elif arr[j]==1:
                j-=1
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        return arr
sol = Solution()
print(sol.segregate0and1([0,0,0,1,0,0,0,0,1,1,1,1,1,1]))