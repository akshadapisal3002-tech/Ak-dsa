class Solution :
    def three_sum_closest(self , nums:list[int],target:int)->int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left < right :
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum == target:
                    return closest
                elif curr_sum < target:
                    left+=1
                else:
                    right -= 1
        return closest
                     
                