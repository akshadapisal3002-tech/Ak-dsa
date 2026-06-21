class Solution(object):
    def searchMatrix(self, matrix, target):
        i = 0
        low = 0
        high = len(matrix)-1
        while low <= high:
            guess = (low+high)//2
            if matrix[guess][0]==target:
                return True
            elif matrix[guess][0]<target:
                low = guess+1
            else:
                high = guess-1
        row = high
        low =0
        high = len(matrix[row])-1
        if row < 0:
            return False
        while low<= high:
            guess = (low+high)//2
            if matrix[row][guess]== target:
                return True
            elif matrix[row][guess]< target:
                low = guess+1
            else:
                high = guess-1
        return False