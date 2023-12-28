import sys
import heapq
input=sys.stdin.readline

##입력
INF=sys.maxsize
N,M,X=map(int,input().split()) #N : vertexes, M : edges
graph=[[] for _ in range(N+1)]
#minCost=[INF for _ in range(N+1)] 다익스트라 함수를 여러번 호출해야 하니 minCost를 지역적으로 선언해야하나?

for _ in range(M):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))


##알고리즘

def dijkstra(start:int)->list:
    minCost=[INF for _ in range(N+1)] #!line9
    minCost[start]=0
    minCost[0]=-1
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cost,curNode=heapq.heappop(q)
        if cost<minCost[curNode]:
            continue
        for next in graph[curNode]:
            cost=minCost[curNode]+next[1] #next[1] : weight of next value // #next[0] : next node
            if(cost<minCost[next[0]]):
                minCost[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))

    return minCost

maxTime=0
for i in range(1,N+1):
    time=0
    time+=dijkstra(i)[X] #각 노드에서 X까지 가는 최단거리
    time+=dijkstra(X)[i] #X에서 i로 돌아오는 최단거리
    if(time>maxTime):
        maxTime=time
    
print(maxTime)
