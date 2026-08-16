class Solution():
    def CountOccenece(self,s):
        count = {}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        return count
sol = Solution()
print(sol.CountOccenece("banana"))
