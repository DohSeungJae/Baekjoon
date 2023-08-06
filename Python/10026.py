import sys
from collections import deque
input=sys.stdin.readline
nXs=[1,-1,0,0]
nYs=[0,0,1,-1]
cnt=0
cnt_m=0

def bfs(start,graph,visited):
    q=deque()
    q.append(start)

    while q:
        cord=q.popleft()
        x=cord[0]
        y=cord[1]
        visited[y][x]=1


        for i in range(4):
            nx=x+nXs[i]
            ny=y+nYs[i]

            if(not (0<=nx<n and 0<=ny<n)):
                continue

            if(graph[ny][nx]==graph[y][x] and visited[ny][nx]==0):
                visited[ny][nx]=1
                q.append([nx,ny])

n=int(input())
graph=[]
graph_m=[]

visited=[[0] * n for i in range(n)]
visited_m=[[0] * n for i in range(n)]

for _ in range(n):
    line=input().strip()
    temp=[]
    temp_m=[]

    for c in line:
        temp.append(c)
        if(c=='G'): c='R'
        temp_m.append(c)

    graph.append(temp)
    graph_m.append(temp_m)


for y in range(n):
    for x in range(n):
        if(visited[y][x]==0):
            bfs([x,y],graph,visited)
            cnt+=1

        if(visited_m[y][x]==0):
            bfs([x,y],graph_m,visited_m)
            cnt_m+=1


print(cnt,cnt_m)

