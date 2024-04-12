import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
board=[]
cur=[]
dy=[1,-1,0,0]
dx=[0,0,1,-1]

def bfsFindTarget(cur:list[int,int])->list[int,int,int]:
    global unitSize
    visited=[[0 for _ in range(N)] for _ in range(N)]
    timeOf=[[0 for _ in range(N)] for _ in range(N)]
    eatables=[]
    q=deque()
    q.append([cur[0],cur[1]])
    
    while q:
        y,x=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if(not(0<=ny<N and 0<=nx<N)): #붐위 안에 있는지 체크
                continue
            if(visited[ny][nx]==1): #방문 가능 여부1
                continue
            if(not(unitSize>=board[ny][nx])): #방문 가능 여부2
                continue
            visited[ny][nx]=1
            q.append([ny,nx])
            timeOf[ny][nx]=timeOf[y][x]+1
            
            if(unitSize>board[ny][nx] and board[ny][nx]!=0):
                eatables.append([ny,nx,timeOf[ny][nx]])
    
    eatables.sort(key=lambda x:(x[2],x[0],x[1]))
    return eatables

for y in range(N):
    line=list(map(int,input().split()))
    board.append(line)
    for x in range(N):
        if(line[x]==9):
            cur=[y,x]
            board[y][x]=0

unitSize=2
exp=0
time=0
while 1:
    targets=bfsFindTarget(cur)
    if(len(targets)==0):
        print(time)
        break

    targetY,targetX,distFromTarget=targets[0]
    exp+=1
    if(unitSize==exp):
        exp=0
        unitSize+=1

    board[targetY][targetX]=0
    cur=[targetY,targetX]
    time+=distFromTarget


