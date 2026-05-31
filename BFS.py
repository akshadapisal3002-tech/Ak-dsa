from collections import deque
from typing import List
class Solution:
    def bfs(self, adj):
        V = len(adj)
        visited = [False]* V
        result =[]
        
        q = deque()
        q.append(0)
        visited[0] = True
        
        while q:
            node =q.popleft()
            result.append(node)
            
            for neighbour in adj[node]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    q.append(neighbour)
        return result