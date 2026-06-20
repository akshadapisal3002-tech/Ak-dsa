class Solution:
    def findceil(self,arr,x):
        low = 0
        high = len(arr)-1
        result = -1
        while low <= high:
            guess = (low +high)//2
            if arr[guess]>= x:
                result = guess
                high = guess- 1
            else:
                low = guess+1
        return result
                

