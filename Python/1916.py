import sys
input=sys.stdin.readline
INF=100000001

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
costs=[INF]*(n+1)

def smallest():
    min_cost=INF
    idx=0
    for i in range(1,n+1):
        if not visited[i] and costs[i] < min_cost: #방문하지 않은 노드들 중 최솟값
            min_cost=costs[i]
            idx=i
    
    return idx

def dijkstra(start):
    costs[start]=0
    visited[start]=True
    
    for i in graph[start]:
        costs[i[0]]=min(costs[i[0]],i[1])

    for _ in range(n-1):
        cur=smallest()
        visited[cur]=True

        for next in graph[cur]:
            cost_ac=costs[cur]+next[1]
            if cost_ac<costs[next[0]]:
                costs[next[0]]=cost_ac

for _ in range(m):
    dep,des,cost=map(int,input().split())
    
    graph[dep].append([des,cost])
    #여기에 중복처리 코드

a,b=map(int,input().split())

print(graph)

dijkstra(a)
print(costs[b])
