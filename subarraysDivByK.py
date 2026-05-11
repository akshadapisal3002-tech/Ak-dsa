class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sum_p = 0
        fre = {0:1}

        for i in range (len(nums)):
            sum_p += nums[i]

            reminder = sum_p % k

            if reminder < 0:
                reminder += k
            count += fre.get(reminder,0)
            fre[reminder] = fre.get(reminder,0)+1
        return count

        