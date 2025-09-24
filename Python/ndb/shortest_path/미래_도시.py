import sys
input=sys.stdin.readline
INF=sys.maxsize

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
x,k=map(int,input().split())

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            graph[s][e]=min(graph[s][e],graph[s][k]+graph[k][e])

x=graph[1][k]
y=graph[k][x]
if(x==INF or y==INF or (x+y)==INF):
    print(-1)
else:
    print(x+y)

