import sys
from collections import deque
input=sys.stdin.readline

def bfs(v):
    q=deque()
    q.append(v)
    cnt=1
    while q:
        v=q.popleft()
        x=v[0]
        y=v[1]
        graph[y][x]=0
        for i in range(4):
            nextX=x+aroundX[i]
            nextY=y+aroundY[i]

            if(0<=nextX<n and 0<=nextY<n):
                if(graph[nextY][nextX]==1):
                    graph[nextY][nextX]=0
                    q.append([nextX,nextY])
                    cnt+=1

    return cnt
    

n=int(input())
graph=[[0]*n for i in range(n)]
aroundX=[1,-1,0,0]
aroundY=[0,0,1,-1]
cnts=[]

for y in range(n):
    line=input().strip()
    for x in range(n):
        graph[y][x]=int(line[x])
    
for y in range(n):
    for x in range(n):
        if(graph[y][x]==1):
            cnts.append(bfs([x,y]))



cnts.sort()

print(len(cnts))
for i in cnts:
    print(i)

