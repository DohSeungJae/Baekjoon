import sys
import heapq
input=sys.stdin.readline
INF=sys.maxsize

N,E=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2=map(int,input().split())

def dijkstra(start:int,dest:int)->int:
    minCost=[INF for _ in range(N+1)]
    minCost[0]=-1
    minCost[start]=0

    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cost,cur=heapq.heappop(q)
        if(cost<minCost[cur]):
            continue
        for next in graph[cur]:
            cost=minCost[cur]+next[1]
            if(cost<minCost[next[0]]):
                minCost[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))

    return minCost[dest]

way1=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N)
way2=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N)

if(way1>=INF or way2>=INF or dijkstra(1,N)>=INF):
    print(-1)
else:
    print(min(way1,way2))