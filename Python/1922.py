import sys
import heapq
input=sys.stdin.readline

N=int(input())
M=int(input())

graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

hq=[(0,1)]
cnt=0
ans=0

while hq:
    if(cnt==N):
        break
    cost,node=heapq.heappop(hq)
    if(not visited[node]):
        visited[node]=True
        ans+=cost
        cnt+=1
        for next in graph[node]:
            heapq.heappush(hq,next)

print(ans)
