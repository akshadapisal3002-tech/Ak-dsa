class Solution(object):
    def reverseString(self, s):
        
        stack = []
        for ch in s:
            stack.append(ch)
        for i in range(len(s)):
            s[i]=stack.pop()
        return stack