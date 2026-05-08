#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        n = len(A)
        i = 0
        best_ending = A[0]
        ans = A[0]
        
        for i in range(1,n):
            v1 = best_ending + A[i]
            v2 = A[i]
            best_ending = min(v1,v2)
            ans = min(ans,best_ending)
        return ans
        