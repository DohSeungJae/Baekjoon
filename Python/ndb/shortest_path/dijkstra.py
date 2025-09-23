import sys
import heapq
input=sys.stdin.readline
INF=sys.maxsize

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    d[start]=0
    while q:
        dist,now=heapq.heappop(q)
        #노드 선택(방문)
        if(d[now]<dist):
            #선택된 노드로 가는 최단 거리 값(dist)이 이미 기록된 거리 테이블(d[now])의 값보다 크다면 이미 방문한 것으로 간주.
            #우선순위 큐를 사용하기 때문에 거리 테이블의 값이 더 작다면 이미 이전에 처리되었을 것임.

            continue
            #이미 처리된 경우이므로 스킵.

        #하지만 결론적으로 위 조건문이 없어도 시간복잡도는 동일함.
        for i in graph[now]:
            next_d,next_n=i[0],i[1]
            cost=dist+next_d
            if(cost<d[next_n]):
                #조건에 맞으면 인접한 노드의 최단 거리 갱신 <- 노드를 선택(방문)한 것은 아님.
                #힙큐에 추가하여 거리가 적은 것 순으로 방문 예정.
                d[next_n]=cost
                heapq.heappush(q,(cost,next_n))



        
n,m=map(int,input().split())
start=int(input())

graph=[[] for _ in range(n+1)]
d=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))

dijkstra(start)

for i in range(1,n+1):
    if(d[i]==INF):
        print("INFINITY")
    else:
        print(d[i])
