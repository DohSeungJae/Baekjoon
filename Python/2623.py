import sys
from collections import deque
input=sys.stdin.readline

class TopologicalSort:
    def __init__(self,vertex:int)->None:
        self.v=vertex
        self.graph=[[] for _ in range(self.v)]
    
    def addEdge(self,u:int,v:int)->None:
        self.graph[u].append(v)
    
    def topologicalSort(self)->list[int]:
        inDegree=[0]*self.v
        for i in range(self.v):
            for j in self.graph[i]:
                inDegree[j]+=1

        q=deque()
        for i in range(self.v):
            if(inDegree[i]==0):
                q.append(i)
        
        res=[]
        while q:
            n=q.popleft()
            res.append(n)

            for i in self.graph[n]:
                inDegree[i]-=1
                if(inDegree[i]==0):
                    q.append(i)

        return res

N,M=map(int,input().split())
g=TopologicalSort(N+1)
for _ in range(M):
    temp=list(map(int,input().split()))
    for i in range(1,len(temp)-1):
        g.addEdge(temp[i],temp[i+1])

res=g.topologicalSort()[1:]
if(len(res)<N):
    print(0)
    exit(0)
for i in res:
    print(i)
