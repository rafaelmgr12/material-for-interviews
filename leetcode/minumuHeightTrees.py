from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        edges_cnt = {}
        leaves = deque()
        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edges_cnt[src] = len(neighbors)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            lenght = len(leaves)
            for _ in range(lenght):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edges_cnt[nei] -= 1
                    if edges_cnt[nei] == 1:
                        leaves.append(nei)
                        
        return list(leaves)
    