class Solution():
    def MaxSubArry(self,nums):
        maximum = nums[0]
        curr_sum = nums[0]

        for i in range(1,len(nums)):
            curr_sum = max(nums[i],curr_sum+nums[i])
            maximum = max(maximum,curr_sum)
        return maximum