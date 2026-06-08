class Solution:
    def triplets_with_smaller_sum(self,arr,num):
        arr.sort()
        target = 0

        for i in range(len(num)-2):
            left = i+1
            right = len(num)-1

            while left < right:
                a = arr[i]+arr[left]+arr[right]
                if s> target:
                    right -=1
                else:
                    target = target +(right-left)
                    left +=1
        return target 