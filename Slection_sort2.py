class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        
        for i in range(n-1):
            samllest = i

            for j in range(i+1,n):
                if nums[j]<nums[samllest] :
                    samllest =j
            nums[i] ,nums[samllest] = nums[samllest],nums[i]
        return nums
