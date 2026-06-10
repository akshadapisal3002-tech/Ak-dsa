from collections import Counter
class Solution:
    def preumutation(self,s1:str,s2:str)->bool:
        n =len(s1)
        if n > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter()

        for i in range(len(s2)):
            window[s2[i]]+=1

            if i >= n:
                window[s2[i-n]]-=1
                if window[s2[i-n]]==0:
                    del window[s2[n-1]]

            if window == need:
                return True
        return False  
