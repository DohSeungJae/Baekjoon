import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

visited=[0]*100001
minCost=[0]*100001
vertexFrom={}

N,K=map(int,input().split())
def bfs(v:int)->None:
    q=deque()
    q.append(v)
    visited[v]=1

    while len(q)>0:
        v=q.popleft()
        if(v==K):
            break
        for next in (v-1,v+1,2*v):
            if(next>100000 or next<0):
                continue
            if(visited[next]==0):
                visited[next]=1
                minCost[next]=minCost[v]+1
                q.append(next)
                if(next not in vertexFrom.keys()):
                    vertexFrom[next]=v

def printPath(cur:int)->None:
    if(cur==N):
        print(cur,end=" ")
        return 
    printPath(vertexFrom[cur])
    print(cur,end=" ")


bfs(N)
print(minCost[K])
printPath(K)
