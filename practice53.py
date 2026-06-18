class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
            odd= False
            res = 0
            for val in freq.values():
                if val %2 ==0:
                    res+=val
                else:
                    res+=val-1
            if odd :
                return res+1
        return res