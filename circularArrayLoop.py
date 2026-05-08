class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def next_index(i):
            return(i+nums[i])%n
        for i in range(n):
            slow = i
            fast = i
            direction = nums[i] > 0
            while True:
                slow = next_index(slow)
                if (nums[slow]>0) != direction:
                    break
                fast = next_index(fast)
                if(nums[fast]>0) != direction:
                    break
                fast = next_index(fast)
                if (nums[fast]>0) != direction:
                    break
                if slow == next_index(slow):
                    break
                if slow == fast :
                    return True
        return False