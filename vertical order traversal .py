'''
class Node:
    def __init__(self, val=0,left=None,right=None):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import defaultdict,deque
class Solution:
    def verticalOrder(self, root): 
        # code here
        if not root:
            return []
        q=deque([(0,0,root)])
        d=defaultdict(lambda:defaultdict(list))
        while(len(q)>0):
            vertical,level,node=q.popleft()
            if (node.left):
                q.append((vertical-1,level+1,node.left))
            if (node.right):
                q.append((vertical+1,level+1,node.right))
            d[vertical][level].append(node.data)
        ans=[]
        for i in sorted(d):
            col=[]
            for j in sorted(d[i]):
                col.extend(d[i][j])
            ans.append(col)
        return ans
        
