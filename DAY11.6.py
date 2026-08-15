class Solution():
    def Second_largest(self,arr,):
        first = float('-inf')
        second = float('-inf')

        for num in arr:
            if num > first:
                second = first
                first = num
            if num < first and num < second:
                second = num
        return second
    
sol = Solution
print(sol.Second_largest([10,20,304,50]))