class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        
        while low < high:
            guess = (low+high)//2
            if nums[guess]>nums[high]:
                low = guess+1
            else:
                high = guess
        return nums[low]