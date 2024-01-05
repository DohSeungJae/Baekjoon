import sys
import heapq
input=sys.stdin.readline

V,E=map(int,input().split())
visited=[False]*(V+1)
graph=[[] for _ in range(V+1)]

for _ in range(E):
    A,B,C=map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

ans=0
cnt=0
hq=[(0,1)]
while hq:
    if(cnt==V):
        break
    w,s=heapq.heappop(hq)
    if not visited[s]:
        visited[s]=True
        ans+=w
        cnt+=1
        for i in graph[s]:
            heapq.heappush(hq,i)

print(ans)

#Prim's        

