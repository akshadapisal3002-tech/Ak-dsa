class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square(nums):
            total = 0
            while nums > 0:
                digit = nums% 10
                total += digit **2
                nums//= 10
            return total
        slow = n
        fast = n

        while True :
            slow = sum_square(slow)
            fast = sum_square(sum_square(fast))

            if fast == 1:
                return True
            if slow == fast :
                return False
