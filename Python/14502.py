import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
viruses=[]
spaces=[]
board=[]
walls=[]
secured=N*M
aroundY=[1,-1,0,0]
aroundX=[0,0,1,-1]
safe=0

for y in range(N):
    line=list(map(int,input().split()))
    for x in range(len(line)):
        if(line[x]==2):
            secured-=1
            viruses.append([y,x])
        elif(line[x]==1):
            secured-=1
        else:
            spaces.append([y,x])
    board.append(line)


def bt(start:int)->None:
    global secured
    global safe
    if(len(walls)==3):
        safe=max(safe,bfs(viruses))
        return
    for i in range(start,len(spaces)):
        if(spaces[i] not in walls):
            walls.append(spaces[i])
            board[spaces[i][0]][spaces[i][1]]=1
            bt(i+1)
            walls.pop()
            board[spaces[i][0]][spaces[i][1]]=0

def bfs(startList:list)->int:
    visited=[[0 for _ in range(M)] for _ in range(N)]
    virusCnt=0

    for start in startList:
        q=deque()
        q.append(start)
        while q:
            cur=q.popleft()
            y=cur[0]
            x=cur[1]
            visited[y][x]=1

            for i in range(4):
                nextX=x+aroundX[i]
                nextY=y+aroundY[i]

                if(0<=nextX<M and 0<=nextY<N):
                    if(visited[nextY][nextX]==0 and
                    board[nextY][nextX]==0):
                        visited[nextY][nextX]=1
                        virusCnt+=1
                        q.append([nextY,nextX])

    
    return secured-virusCnt-3
                

bt(0)
print(safe)

