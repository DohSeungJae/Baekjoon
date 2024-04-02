import sys
from collections import deque
input=sys.stdin.readline
minDist=sys.maxsize

N,M=map(int,input().split())
graph=[]
walls=[]
aroundX=[1,-1,0,0]
aroundY=[0,0,1,-1]

def bfs(start:list,visited:list)->None:
    q=deque()
    q.append(start)
    while q:
        cur=q.popleft()
        y,x=cur[0],cur[1]

        for i in range(4):
            nextY=y+aroundY[i]
            nextX=x+aroundX[i]
            if not(0<=nextX<M and 0<=nextY<N):
                continue
            if(graph[nextY][nextX]==0 and visited[nextY][nextX]==0):
                visited[nextY][nextX]+=1
                q.append([nextY,nextX])

    if(visited[N-1][M-1]==1):
        return sys.maxsize
    
    return distOf[N-1][M-1]

for y in range(N):
    line=input().strip()
    line=[int(i) for i in line]
    for x in range(M):
        if(line[x]==1):
            walls.append([y,x])
    graph.append(line)


if not walls:
    visited=[[0]*M for _ in range(N)]
    distOf=[[0]*M for _ in range(N)]
    minDist=min(bfs([0,0],visited),minDist)

for wall in walls:
    visited=[[0]*M for _ in range(N)]
    distOf=[[0]*M for _ in range(N)]
    
    graph[wall[0]][wall[1]]=0
    minDist=min(bfs([0,0],visited),minDist)
    graph[wall[0]][wall[1]]=1

if(N==M==1):
    minDist=1

elif(minDist==sys.maxsize):
    minDist=-1

print(minDist)
