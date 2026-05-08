class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        nodelete = arr[0]
        one_delete = arr[0]
        ans = arr[0]

        for i in range(1,n):
            one_delete = max(one_delete+arr[i],nodelete)

            nodelete = max(nodelete+arr[i],arr[i])

            ans = max(ans,max(one_delete,nodelete))
        return ans


        