import sys
from collections import deque
input=sys.stdin.readline

def bfs(start):
    cnt=0
    q=deque()
    q.append(start)
    x=start[0]
    y=start[1]

    visited[y][x]=1
    graph[y][x]='O'

    while q:
        cor=q.popleft()
        x=cor[0]
        y=cor[1]

        for i in range(4):
            nextX=x+around_x[i]
            nextY=y+around_y[i]

            if((0<=nextX<m) and (0<=nextY<n)):
                next=graph[nextY][nextX]
                if((next!='X') and visited[nextY][nextX]==-1):
                    if next=='P': cnt+=1
                    visited[nextY][nextX]=1
                    q.append([nextX,nextY])

    return cnt
                
n,m=map(int,input().split())

graph=[["O"]*m for i in range(n)]
visited=[[-1]*m for i in range(n)]
around_x=[1,-1,0,0]
around_y=[0,0,1,-1]
start=[-1,-1]

for y in range(n):
    line=input().strip()
    for x in range(m):
        graph[y][x]=line[x]
        if(graph[y][x]=="I"): start=[x,y]

cnt=bfs(start)

if cnt==0: print("TT")
else: print(cnt)
