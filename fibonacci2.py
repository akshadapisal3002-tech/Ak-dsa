class Solution:
    def fibonacci(self,n):
        if n ==0 :
            return 0
        if n ==1 :
            return 1
        ans1 = self.fibonacci(n-1)
        ans2 = self.fibonacci(n-2)
        result = ans1+ans2
        return result
sol = Solution()
print(sol.fibonacci(10))