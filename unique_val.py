<<<<<<< HEAD

=======
>>>>>>> 1d83e716e87d7f8bf8d7957944b3f26bc5a4fff9
class Solution:
    def deleteDuplicates(self, a: List[int]) -> List[int]:
        if not a:
            return []

        i = 0              
        j = 1              

        while j < len(a):
            if a[j] != a[i]:      
                i += 1            
                a[i] = a[j]       
            j += 1                

        return a[:i+1] 
