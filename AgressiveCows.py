class Solution:
    def aggressiveCows(self, stalls, k):

        def canPlace(stalls, k, dist):
            count = 1
            lastPlaced = stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] - lastPlaced >= dist:
                    lastPlaced = stalls[i]
                    count += 1
                if count == k:
                    return True
            return False

        stalls.sort()
        low = 1
        high = stalls[-1] - stalls[0]
        res = -1

        while low <= high:
            guess = (low + high) // 2

            if canPlace(stalls, k, guess):
                res = guess
                low = guess + 1    
            else:
                high = guess - 1   

        return res