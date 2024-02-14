import sys
from collections import deque
input=sys.stdin.readline

visited=[0]*100001
minCost=[0]*100001
path=[0]*100001
N,K=map(int,input().split())

def bfs(v):
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
                path[next]+=1
                q.append(next)
            elif(minCost[next]==minCost[v]+1):
                path[next]+=1
                q.append(next)

bfs(N)
if(N==K):
    print(0)
    print(1)
    exit(0)

print(minCost[K])
print(path[K])

