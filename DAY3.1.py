class Solution():
    def Two_Sum(self,arr,target):
        i = 0
        j = len(arr)-1

        while i < j:
            Sum_of = arr[i]+arr[j]
            if Sum_of == target:
                return i,j
            
            elif Sum_of <target:
                i+=1
            else:
                j-=1
        return 
    
Sol = Solution()
result = Sol.Two_Sum([2,3,4,7,11,15],9)
print(result)