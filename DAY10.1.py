class Solution():
    def smallest(self,nums,target):
        left = 0
        curr_sum =0
        minimum =float(-'inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                length = right-left+1

                if length < minimum:
                    minimum = length

                curr_sum -=nums[left]
                left+=1
        if minimum ==float(-'inf'):
            return 0
        return minimum
