class Solution:
    def Palindrom(self,n):
        if n <0:
            return False
        original = n
        reversed_num = 0
        while n > 0:
            digit = n%10
            reversed_num = reversed_num * 10 +digit
            n = n//10
        return original == reversed_num
    def palindrom2(self,s):
        s = str(s)
        return s == s[::-1]
sol = Solution
print(sol.Palindrom(121))
print(sol.palindrom2("madam"))
    
