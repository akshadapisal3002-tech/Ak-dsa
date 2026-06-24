class Solution:
    def SumOfdigits(self,n):
        if n ==0:
            return 0
        d = n%10
        n = n//10
        ans = self.SumOfdigits(n)
        result = ans+d
        return result