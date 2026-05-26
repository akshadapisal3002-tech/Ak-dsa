class Solution:
    def isSorted(self, arr, i = 0, n = None ) -> bool:
        if n is None:
            n = len(arr)
            
        if i == n or i == n-1:
            return True
        if arr[i]> arr[i+1]:
            return False
        return self.isSorted(arr,i+1,n)
        