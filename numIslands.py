from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0]* m for _ in range(n)]

        x =[-1,1,0,0]
        y = [0,0,1,-1]

        def validation(i,j):
            if i < 0 or i >= n or j < 0 or j>= m :
                return False
            return True 
        def dfs(i,j):
            visited[i][j] = 1

            for k in range(4) :
                row = i + x[k]
                col = j + y[k]
                if validation(row , col) and grid[row][col]== '1' and visited[row][col]==0:
                    dfs(row , col)
        count = 0
        for i in range(n):
           for j in range(m):
                if grid[i][j] == '1' and visited [i][j]== 0:
                    dfs(i ,j)
                    count += 1
        return count


