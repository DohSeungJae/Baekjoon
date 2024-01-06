import sys
import heapq
input=sys.stdin.readline

N=int(input())
graph=[[] for _ in range(N)]
visited=[False for _ in range(N)]

for i in range(N):
    line=list(map(int,input().split()))
    for j in range(N):
        if(line[j]==0):
            continue
        graph[i].append((line[j],j))

hq=[(0,0)]
cnt=0
totalCost=0

while hq:
    if(cnt==N):
        break
    cost,node=heapq.heappop(hq)
    if(not visited[node]):
        visited[node]=True
        cnt+=1
        totalCost+=cost
        for next in graph[node]:
            heapq.heappush(hq,next)

print(totalCost)


