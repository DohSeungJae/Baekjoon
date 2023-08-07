import sys
from collections import deque
input=sys.stdin.readline

m,n,h=map(int,input().split())
graph=[]
starts=[]

visited=[[[0]* m for i in range(n)] for i in range(h)]
aroundX=[1,-1,0,0,0,0]
aroundY=[0,0,1,-1,0,0]
aroundZ=[0,0,0,0,1,-1]
isZero=0

def bfs(day):
    cnt=0
    q=deque()

    while q or day:
        for i in day:
            q.append(i)
        day=[]

        while q:
            xyz=q.popleft()
            x=xyz[0]
            y=xyz[1]
            z=xyz[2]
            visited[z][y][x]=1

            for i in range(6):
                nx=x+aroundX[i]
                ny=y+aroundY[i]
                nz=z+aroundZ[i]

                if(0<=nx<m and 0<=ny<n and 0<=nz<h):
                    if(graph[nz][ny][nx]==0 and
                       visited[nz][ny][nx]==0):
                        visited[nz][ny][nx]=1
                        day.append([nx,ny,nz])

        if day: cnt+=1

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if(visited[z][y][x]==0 and graph[z][y][x]==0):
                    cnt=-1

    return cnt



for z in range(h):
    twoDgraph=[]
    for y in range(n):
        temp=list(map(int,input().split()))
        if 0 in temp:
            isZero+=1
        if 1 in temp:
            for x in range(m):
                if(temp[x]==1):
                    starts.append([x,y,z])

        twoDgraph.append(temp)

    graph.append(twoDgraph)


if(bool(isZero)==False):
    print(0)
    exit(0)


print(bfs(starts))

