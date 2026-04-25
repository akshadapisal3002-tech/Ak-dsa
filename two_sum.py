class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(a)-1
       
        while i<j: 
            sum = a[i]+a[j]
            if sum == target:
                return [i+1,j+1]
            elif sum < target:
                 i += 1
            else :
                j -= 1
        return Null