class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        target = 0

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                sum = arr[i] + arr[left] + arr[right]

                if sum >= target:
                    right -= 1
                else:
                    target = target + (right - left)
                    left += 1

        return target