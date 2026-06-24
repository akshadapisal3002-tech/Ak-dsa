class Solution:
    def removeCharacters(self,s,c,i=0,n=None):
        if n is None:
            n = len(s)
        if i ==n:
            return ""
        ans =self.removeCharacters(s,c,i+1,n)
        if s[i]==c:
            return ans
        return s[i]+ans
s= input()
c= input()
obj = Solution()
print(obj.removeCharacters(s,c))
             