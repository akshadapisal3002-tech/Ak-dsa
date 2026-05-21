class Solution(object):
    def minEatingSpeed(self, piles, h):
        def fun(a, n, speed):
            hours = 0
            for i in range(n):
                hours = hours + a[i] // speed
                if a[i] % speed != 0:
                    hours += 1
            return hours

        n = len(piles)
        low = 1
        high = max(piles)
        res = -1

        while low <= high:
            guess = (low + high) // 2
            hours = fun(piles, n, guess)

            if hours > h:       
                low = guess + 1
            else:              
                res = guess
                high = guess - 1

        return res
