class Solution():
    def palindrom(self,str):
        if not str:
            return None
        
        i = 0
        j = len(str)

        while i< j:
            if str[i] != str[j]:
                return False
            i+=1
            j-=1
        return True
    
sol = Solution()
print(sol.palindrom("madam"))
