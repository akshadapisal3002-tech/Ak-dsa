class Solution():
    def factotial(self,n):
        if n < 0:
            return None
        result = 1
        for i in range(2,n+1):
            result *= i
        return result
    def factorial_recursive(self,n):
        if n < 0:
            return None 
        if n ==0 or n ==1:
            return 1
        return n * self.factorial_recursive(n-1)
sol = Solution()
print(sol.factorial_recursive(10))
print(sol.factotial(5))

