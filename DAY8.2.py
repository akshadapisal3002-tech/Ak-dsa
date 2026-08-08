class Solution():
    def findMissingNum(self,arr):
        n = len(arr)+1

        excepted = n*(n+1)/2

        actual = 0

        for i in range(len(arr)):
            actual +=arr[i]

        return excepted - actual
sol = Solution()
print(sol.findMissingNum([1,2,3,5,6]))
