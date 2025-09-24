import sys
input=sys.stdin.readline
INF=sys.maxsize
import heapq

n,m,c=map(int,input().split())
graph=[[] for _ in range(n+1)]
d=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((z,y))

def dijkstra(start:int)->None:
    q=[]
    heapq.heappush(q,(0,start))
    d[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if(d[now]<dist):
            continue

        for (next_d,next_n) in graph[now]:
            cost=d[now]+next_d
            if(cost<d[next_n]):
                d[next_n]=cost
                heapq.heappush(q,(cost,next_n))

dijkstra(c)

maxi=0
cnt=0
for i in d:
    if(i==0 or i==INF):
        continue
    maxi=max(maxi,i)
    cnt+=1

print(cnt,maxi)


