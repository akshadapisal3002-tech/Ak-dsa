class Solution:
    def deleteDuplicates(self, a):
        if not a :
            return[]
        
        i =0
        j = 1

        while j<len(a):
            if a[i]!=a[j]:
                i+=1
                a[i]=a[j]
            j+=1
        return a[:i+1]

            
        
sol = Solution()
print(sol.deleteDuplicates([1,2,3,4,4,5,6,6,7,8]))