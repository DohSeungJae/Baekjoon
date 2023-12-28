import sys
import heapq
input=sys.stdin.readline

##입력, 상수 선언
V,E=map(int,input().split())
INF=sys.maxsize
arr=[[] for _ in range(V+1)]
minCost=[INF for _ in range(V+1)]

start=int(input())
minCost[start]=0
minCost[0]=-1

##입력 처리
for _ in range(E):
    u,v,w=map(int,input().split())
    arr[u].append((v,w))


##다익스트라 알고리즘(heapq)
def dijkstra(start):

    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cost,cur=heapq.heappop(q)
        if cost<minCost[cur]:
            continue
        for nextNode in arr[cur]:
            cost=minCost[cur]+nextNode[1]
            if (cost<minCost[nextNode[0]]):
                minCost[nextNode[0]]=cost
                heapq.heappush(q,(cost,nextNode[0]))


dijkstra(start)

for i in range(1,V+1):
    if(minCost[i]==INF):
        print("INF")
    else:
        print(minCost[i])
        

