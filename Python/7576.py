import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
graph=[]
starts=[]
visited=[[0]*m for i in range(n)]
aroundX=[1,-1,0,0]
aroundY=[0,0,1,-1]
isZero=0

def bfs(day):
    cnt=0
    q=deque()

    while q or day:

        for i in day:
            q.append(i)
        day=[]

        while q:
            xy=q.popleft()
            x=xy[0]
            y=xy[1]
            visited[y][x]=1

            for i in range(4):
                nextX=x+aroundX[i]
                nextY=y+aroundY[i]

                if(0<=nextX<m and 0<=nextY<n):
                    if(graph[nextY][nextX]==0 and 
                       visited[nextY][nextX]==0):
                        visited[nextY][nextX]=1
                        graph[nextY][nextX]=1
                        day.append([nextX,nextY])

        if day: cnt+=1

    for y in range(n):
        for x in range(m):
            if(visited[y][x]==0 and graph[y][x]==0):
                cnt=-1


    return cnt
                    
for y in range(n):
    temp=list(map(int,input().split()))
    if 0 in temp:
        isZero+=1
    if 1 in temp:
        for x in range(m):
            if(temp[x]==1):
                starts.append([x,y]) 
    graph.append(temp)

if(bool(isZero)==False):
    print(0)
    exit(0)

print(bfs(starts))





