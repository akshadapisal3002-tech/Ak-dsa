class Solution:
    def bubbleSort(self, nums):
        for i in range(n-1):
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1]= nums[j+1],nums[j+1]
        return nums

