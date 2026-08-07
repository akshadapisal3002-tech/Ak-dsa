class Solution():
    def Secondlargest(self,arr):
        first = float('inf')
        second = float('inf')

        for num in arr:
            if num > first:
                second = first
                first = num
            elif num <first and num> second:
                second = num
        return second
    
sol = Solution()
print(sol.Secondlargest([10,20,30,40,50,60,70]))