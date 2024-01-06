import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
visited=[False for _ in range(N+1)]
graph=[[] for _ in range(N+1)]

originalCost=0
savedCost=0
cnt=0

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    originalCost+=c

hq=[(0,1)]
while hq:
    if(cnt==N):
        break
    cost,node=heapq.heappop(hq)
    if(not visited[node]):
        visited[node]=True
        savedCost+=cost
        cnt+=1
        for next in graph[node]:
            heapq.heappush(hq,next)
            
for i in range(1,N+1):
    if(visited[i]==False):
        print(-1)
        exit(0)
        
print(originalCost-savedCost)




