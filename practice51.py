from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = Counter(magazine)
        for ch in ransomNote:
            if freq[ch]==0:
                return False
            freq [ch]-= 1
        return True
