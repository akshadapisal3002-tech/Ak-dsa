class Solution():
    def swap(self,a,b):
        a,b = b,a
        return a,b
sol = Solution()
print(sol.swap(6,5))