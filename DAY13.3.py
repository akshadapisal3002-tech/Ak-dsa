class Solution():
    def Armstorng(self,n):
        original = 0
        digits  = len(str(n))
        total =0

        while n < 0:
            digit = n%10
            totoal += digits* digits
            n = n//10

        return total == original
sol = Solution()
print(sol.Armstorng(123))
