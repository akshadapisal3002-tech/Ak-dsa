class Solution:
    def kthsmallest(self,matrix,k):
        n = len(matrix)
        def countlessEqual(mid):
            count =0
            row =0
            col =n-1
            while row <n and col >= 0:
                if matrix[row][col]<=mid:
                    count += col +1
                    row +=1
                else:
                    col-= 1
            return count
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        res = low
        while low <= high:
            mid = (low+high)//2
            if countlessEqual(mid)<k:
                low = mid+1
            else:
                res =mid
                high = mid-1
        return res
                