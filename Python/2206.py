import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
board=[]
distOf=[[[0]*2 for _ in range(M)] for _ in range(N)]
aroundX=[1,-1,0,0]
aroundY=[0,0,1,-1]

def bfs(start:list[int,int,int])->int:
    q=deque()
    q.append(start)
    distOf[start[0]][start[1]][0]=1
    distOf[start[0]][start[1]][1]=1

    while q:
        cur=q.popleft()
        y,x,w=cur[0],cur[1],cur[2]

        for i in range(4):
            nextY=y+aroundY[i]
            nextX=x+aroundX[i]
            nextW=0
            if(not(0<=nextY<N and 0<=nextX<M)):
                continue

            elif(board[nextY][nextX]==0):
                if(distOf[y][x][1]>0 and w==1 and not y==x==0):
                    nextW=1
                if(distOf[nextY][nextX][nextW]!=0):
                    continue
                distOf[nextY][nextX][w]=distOf[y][x][w]+1
            
            elif(board[nextY][nextX]==1):
                if(distOf[y][x][1]>0 and w==1 and not y==x==0):
                    continue
                distOf[nextY][nextX][1]=distOf[y][x][0]+1
                nextW=1
            
            q.append([nextY,nextX,nextW])

    if(sum(distOf[N-1][M-1])==0):
        return -1
    elif(distOf[N-1][M-1][0]>0 and distOf[N-1][M-1][1]>0):
        return min(distOf[N-1][M-1])
    else:
        return sum(distOf[N-1][M-1])
    
for _ in range(N):
    board.append([int(i) for i in input().strip()])

print(bfs([0,0,0]))
