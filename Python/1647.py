import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
visited=[False for _ in range(N+1)]
graph=[[] for _ in range(N+1)]

for _ in range(M):
    A,B,C=map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

cnt=0
ans=0
hq=[(0,1)]
maxCost=0
while hq:
    if(cnt==N):
        break
    cost,node=heapq.heappop(hq)
    maxCost=max(maxCost,cost)

    if(not visited[node]):
        visited[node]=True
        cnt+=1
        ans+=cost
        for next in graph[node]:
            heapq.heappush(hq,next)

print(ans-maxCost)


