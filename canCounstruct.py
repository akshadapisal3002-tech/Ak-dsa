class Solution(object):
    def canConstruct(self, ransomNote, magazine):
       
        from collections import Counter
        max_freq = Counter(magazine)
        for ch in ransomNote:
            if max_freq [ch]== 0:
                return False
            max_freq[ch] -=1
        return True
        