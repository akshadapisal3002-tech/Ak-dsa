from typing import Counter
class Solution():
    def Non_repeatingChar(self,s):
        frequency ={}
        for char in s:
            if char in frequency:
                frequency[char]+=1
            else:
                frequency[char]=1
        for char in s:
            if frequency[char]==1:
                return char
        return None