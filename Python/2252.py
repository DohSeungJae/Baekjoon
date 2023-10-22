from collections import deque
import sys
input=sys.stdin.readline

class TopologicalGraph:
    def __init__(self,vertex):
        self.v=vertex
        self.graph=[[] for _ in range(self.v)]

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSort(self):
        indegree=[0]*self.v
        for i in range(self.v):
            for j in self.graph[i]:
                indegree[j]+=1
        
        q=deque()
        for i in range(self.v):
            if indegree[i]==0:
                q.append(i)
        
        res=[]

        while q:
            n=q.popleft()
            res.append(n)

            for i in self.graph[n]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        
        return res
    
if __name__=="__main__":

    n,m=map(int,input().split())
    g=TopologicalGraph(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        g.addEdge(a,b)


    print(*g.topologicalSort()[1:])