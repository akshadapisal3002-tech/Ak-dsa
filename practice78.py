class Solution:
    def palindrom(self,s,low= 0,high=None):
        if high is None:
            high= len(s)-1
        length = high - low + 1
        if length == 0 or length ==1:
            return True
        if s[low] != s[high]:
            return False
        return self.palindrom(s,low+1,high-1)