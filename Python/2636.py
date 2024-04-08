import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
board=[]
aroundY=[1,-1,0,0]
aroundX=[0,0,1,-1]

def checkSpace(board:list[list[int]],start:list[int,int]):
    visited=[[0]*M for _ in range(N)]
    q=deque()
    q.append(start)
    visited[start[0]][start[1]]=1
    board[start[0]][start[1]]=-1

    while q:
        cur=q.popleft()
        y,x=cur[0],cur[1]
        for i in range(4):
            nextY=y+aroundY[i]
            nextX=x+aroundX[i]
            if(not(0<=nextY<N and 0<=nextX<M)):
                continue
            if(visited[nextY][nextX]==1):
                continue
            if(board[nextY][nextX]==1):
                continue
            board[nextY][nextX]=-1
            visited[nextY][nextX]=1
            q.append([nextY,nextX])

def deleteTarget(board:list[list[int]],cheeses:list[list[int,int]])->int:
    targets=[]
    for cheese in cheeses:
        y,x=cheese[0],cheese[1]
        if(board[y][x]!=1):
            continue
        aroundCnt=0
        for i in range(4):
            nextY=y+aroundY[i]
            nextX=x+aroundX[i]
            if(not(0<=nextY<N and 0<=nextX<M)):
                continue
            if(board[nextY][nextX]==-1):
                aroundCnt+=1
        if(aroundCnt>=1):
            targets.append([y,x])
                
    for target in targets:
        y,x=target[0],target[1]
        board[y][x]=0
    
    return len(targets)
    

cheeses=[]
for y in range(N):
    line=list(map(int,input().split()))
    for x in range(M):
        if(line[x]==1):
            cheeses.append([y,x])
    board.append(line)
cheeseCnt=len(cheeses)
time=0

lastCheeseCnt=0
while cheeseCnt>0:
    checkSpace(board,[0,0])
    lastCheeseCnt=cheeseCnt
    cheeseCnt-=deleteTarget(board,cheeses)
    time+=1

print(time)
print(lastCheeseCnt)


