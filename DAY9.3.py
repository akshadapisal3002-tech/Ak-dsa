class Solution():
    def lenOfLongest(self,arr):
        seen = set()
        left = 0
        maximum = 0

        for right in range(len(arr)):
            while arr[right] in seen:
                seen.remove(arr[left])
                left+=1

            seen.add(arr[right])

            maximum = max(maximum, right - left +1)
        return maximum