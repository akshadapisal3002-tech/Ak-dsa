import heapq
class Solution:
    def mergeArray(self,mat):
        res =[]
        heap =[]
        n = len(mat)
        for i in range(n):
            heapq.heappush(heap,(mat[i][0],i,0))
        while heap :
            value,row,col= heapq.heappop(heap)
            res.append(value)

            if col +1 < len(mat[row]):
                heapq.heappush(heap,(mat[row][col+1],row,col+1))
        return res 