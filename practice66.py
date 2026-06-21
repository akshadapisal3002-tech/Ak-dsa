class Solution:
    def aggressiveCows(self, stalls, k):
        def canplace(stalls,k,dist):
            count =1
            lastplace = stalls[0]
            for i in range(1,len(stalls)):
                if stalls[i]- lastplace >= dist:
                    lastplace = stalls[i]
                    count +=1
                if count ==k:
                    return True
            return False
        
        stalls.sort()
        low = 0
        high = stalls[-1]-stalls[0]
        res = -1
        while low <= high:
            guess=(low+high)//2
            if canplace(stalls,k,guess):
                res = guess
                low = guess+1
            else:
                high = guess -1
        return res
