class Solution:
    def dfs(self, adj):
        V = len(adj)
        visited = [False] * V
        result = []
        
        def search(node):
            result.append(node)
            visited[node] = True
            for i in range(len(adj[node])):
                neighbour = adj[node][i]
                if visited[neighbour] == False:
                    search(neighbour)
            return
        search(0)
        return result