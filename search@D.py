class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m= len(matrix[0])
        row = 0
        col = m-1

        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]< target:
                row +=1
            else:
                col -=1
        return False 