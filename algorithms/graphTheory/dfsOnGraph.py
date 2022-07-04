'''
Given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph..

https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1/#
'''

#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    # def dfsOfGraph(self, V, adj):
    #     # code here
    #     allnodes = {0}
    #     ans, nodes = [],[0]
    #     while len(ans)<V:
    #         node = nodes.pop()
    #         allnodes.add(node)
    #         ans.append(node)
    #         for j in adj[node][::-1]:
    #             if j not in allnodes:
    #                 nodes.append(j)
    #     return ans
    def dfsOfGraph(self, V, adj):
        ans = []
        self.dfs(0,set(),adj,ans)
        return ans
        
    def dfs(self,node,allnodes,adj,ans):
        if node in allnodes:return
        ans.append(node)
        allnodes.add(node)
        for i in adj[node]:
            if i not in allnodes:
                self.dfs(i,allnodes,adj,ans)



#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends