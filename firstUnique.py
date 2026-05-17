class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        frq = Counter(s)
        for i, ch in enumerate(s):
            if frq[ch]==1:
                return i
        return -1


        