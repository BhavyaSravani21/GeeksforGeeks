class Solution:
    def bfs(self, adj):
        # code here
        vis=[0]*len(adj)
        start=0
        ans=[]
        if (vis[start]==0):
            vis[start]=1
            q=deque([start])
        while (len(q)>0):
            node=q.popleft()#node=0
            for i in adj[node]: #adj[0]=1,2
                if (vis[i]==0):
                    vis[i]=1
                    q.append(i)
            ans.append(node)
        return ans
