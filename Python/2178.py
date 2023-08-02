import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split()) 
graph=[]
aroundX=[1,0,-1,0]
aroundY=[0,1,0,-1]

def mazeBfs(graph,start):
    cnt=1
    q=deque()
    q.append(start)
    graph[0][0]=1
    direct=[]

    while q:
        cord=q.popleft()
        x=cord[0]
        y=cord[1]
        
        for i in range(4):

            nx,ny=x+aroundX[i],y+aroundY[i]
            if(0<=nx<m and 0<=ny<n and graph[ny][nx]==1):
                graph[ny][nx]+=graph[y][x]

                q.append([nx,ny])
            elif(nx==m-1 and ny==n-1): break


        
for i in range(n):
    line=input().strip()
    temp=[]
    for i in line: temp.append(int(i))
    graph.append(temp)


mazeBfs(graph,[0,0])
print(graph[n-1][m-1])

#미로탐색