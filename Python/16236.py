import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
board=[]
loca=[]
fishes=[]
aroundY=[1,-1,0,0]
aroundX=[0,0,-1,1]

def bfsFindTarget(eatables:list[int,int])->None:
    global loca
    target=[-1,-1]
    distFromTarget=sys.maxsize

    for targetFish in eatables:
        sizeOfTarget=board[targetFish[0]][targetFish[1]]
        if(sizeOfTarget==0):
            continue
        if(size<sizeOfTarget):
            continue
        
        q=deque()
        q.append(loca)
        visited=[[0 for _ in range(N)] for _ in range(N)]
        timeOf=[[0 for _ in range(N)] for _ in range(N)]
        visited[loca[0]][loca[1]]=1

        while q:
            cur=q.popleft()
            y,x=cur[0],cur[1]

            for i in range(4):
                nextY=y+aroundY[i]
                nextX=x+aroundX[i]
                if(not(0<=nextY<N and 0<=nextX<N)):
                    continue
                if(visited[nextY][nextX]==1):
                    continue
                if(board[nextY][nextX]>size):
                    continue
                timeOf[nextY][nextX]=timeOf[y][x]+1
                if(targetFish==[nextY,nextX]):
                    if(timeOf[nextY][nextX]<distFromTarget):
                        distFromTarget=timeOf[nextY][nextX]
                        target=[nextY,nextX]
                else:
                    visited[nextY][nextX]=1
                    q.append([nextY,nextX])

    if(target==[-1,-1]):
        return target,-1
    return target,distFromTarget


for y in range(N):
    line=list(map(int,input().split()))
    for x in range(N):
        if(1<=line[x]<=6):
            fishes.append([y,x]) #line[x]는 없어도 상관없음 
        if(line[x]==9):
            loca=[y,x]
    
    board.append(line)

targets=[]
size=2
exp=0
time=0
while 1:
    for fish in fishes:
        if(fish in targets):
            continue
        if(not(0<board[fish[0]][fish[1]]<size)):
            continue
        targets.append(fish)

    target,distFromTarget=bfsFindTarget(targets)
    print(target,distFromTarget)
    if(distFromTarget==-1):
        break
    

    time+=distFromTarget
    board[target[0]][target[1]]=0
    loca=[target[0],target[1]]
    
    exp+=1
    if(size==exp):
        exp=0
        size+=1
        

print(time)


