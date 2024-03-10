"""
323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        adj = {i: [] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        vistit = set()
        def dfs(node):
            if node in vistit:
                return
            
            vistit.add(node)
            for j in adj[node]:
                if j not in vistit:
                    dfs(j)
                    
        count = 0
        
        for i in range(n):
            if i not in vistit:
                count += 1
                dfs(i)
                
        return count
        
        
    def countComponentsDisjoint(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        
        
        def find(n1):
            res = n1
            
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1,p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)        
        return res