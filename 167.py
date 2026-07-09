from typing import List
class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        i =0
        j = len(arr)-1
        while i <j :
            sum_of= arr[i]+arr[j]
            if sum_of == target:
                return i,j
            elif sum_of < target:
                i+=1
            else:
                j-=1
        return 
    
sol = Solution()
print(sol.twoSum([1,2,3,4,5,6,7], 3))                