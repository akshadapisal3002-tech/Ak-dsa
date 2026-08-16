class Solution():
    def CountVowels(self,s):
        vowels = 0
        consonents= 0
        for char in s:
            if char in "aeiouAEIOU":
                vowels+=1
            elif char.isalpha():
                consonents+=1
        return vowels,consonents
sol =Solution()
print(sol.CountVowels("Akshada"))


