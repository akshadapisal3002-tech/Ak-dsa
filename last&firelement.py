class Solution(object):
    def searchRange(self, nums, target):
        
        def findFirst(nums, target):
            low, high, result = 0, len(nums)-1, -1
            while low <= high:
                guess = (low + high) // 2
                if nums[guess] == target:
                    result = guess
                    high = guess - 1   
                    
                elif nums[guess] < target:
                    low = guess + 1
                else:
                    high = guess - 1
            return result

        def findLast(nums, target):
            low, high, result = 0, len(nums)-1, -1
            while low <= high:
                guess = (low + high) // 2
                if nums[guess] == target:
                    result = guess
                    low = guess + 1     
                elif nums[guess] < target:
                    low = guess + 1
                else:
                    high = guess - 1
            return result

        return [findFirst(nums, target), findLast(nums, target)]