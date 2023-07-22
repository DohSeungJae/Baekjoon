import sys
from collections import deque
input=sys.stdin.readline

def bfs(start):
    q=deque()
    q.append(start)
    x=start[0]
    y=start[1]

    graph[y][x]=0
    visited[y][x]=1

    while q:
        cor=q.popleft()
        x=cor[0]
        y=cor[1]

        for i in range(4):
            nextX=x+around_x[i]
            nextY=y+around_y[i]

            if((0<=nextY<n) and (0<=nextX<m)):
                if(graph[nextY][nextX]==1 and visited[nextY][nextX]==-1 ):
                    graph[nextY][nextX]=graph[y][x]+1
                    visited[nextY][nextX]=1
                    q.append([nextX,nextY])
  
    for i in range(n):
        for j in range(m):
            if(graph[i][j]==1 and visited[i][j]==-1):
                graph[i][j]=-1
                       
n,m=map(int,input().split())

around_x=[1,-1,0,0]
around_y=[0,0,1,-1]
idx=[-1,-1]
graph=[]
visited=[[-1]*m for i in range(n)]

for y in range(n):
    temp=list(map(int,input().split()))
    if 2 in temp:
        idx[1]=y

        for x in range(m):
            if(temp[x]==2):
                idx[0]=x

    graph.append(temp)

bfs(idx)

for i in graph:
    for j in i:
        print(j,end=" ")

    print()


    

