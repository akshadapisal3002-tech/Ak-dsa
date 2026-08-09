class Solution():
    def Maxwater(self,arr):
        i= 0
        j = len(arr)-1

        while i< j:
            height =min(arr[i],arr[j])
            width = j-i

            area = height *width

            if area > maximum:
                maximum = area
            
            if arr[i] <arr[j]:
                i+=1
            else:
                j-=1
        return maximum
sol = Solution()
print(sol.Maxwater([1,8,5,2,3,4,6]))