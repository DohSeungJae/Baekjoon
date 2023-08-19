import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n=int(input())

graph=[[] for i in range(n+1)]
parent=[0 for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,visit):
    for i in graph[v]:
        if visit[i]==0:
            visit[i]=v
            dfs(i,visit)


dfs(1,parent)

for i in range(2,n+1):
    print(parent[i])
