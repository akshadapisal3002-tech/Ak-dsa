class Solution():
    def Container_withWater(self,height):
        left =0 
        right= len(height)-1
        max_area= 0

        while left < right:
            width = right -left
            current_area = min(height[left],height[right])*width
            max_area = max(max_area,current_area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
    
sol = Solution()
height=[1,8,2,5,4,8,3,7]
print(sol.Container_withWater(height))