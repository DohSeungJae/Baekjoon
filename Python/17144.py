import sys
input=sys.stdin.readline

A=[]
fu=[]
aroundX=[1,-1,0,0]
aroundY=[0,0,1,-1]

R,C,T=map(int,input().split())

for y in range(R):
    line=list(map(int,input().split()))
    if -1 in line:
        for x in range(C):
            if(line[x]==-1):
                fu.append([y,x])

    A.append(line)


def spread(A:list)->None:
    dusts=[]
    for y in range(R):
        for x in range(C):
            if(A[y][x]>0):
                amount=A[y][x]//5
                dusts.append([y,x,amount])

    for dust in dusts:
        y=dust[0]
        x=dust[1]
        for i in range(4):
            nextY=y+aroundY[i]
            nextX=x+aroundX[i]
            if(not (0<=nextX<C and 0<=nextY<R) or A[nextY][nextX]==-1):
                continue
            
            A[nextY][nextX]+=dust[2]
            A[y][x]-=dust[2]      
    return  

def cycleAndFurify(A:list,f:list)->None:
    idx=0
    startY=f[0][0]
    startX=f[0][1]
    cur=[startY,startX]
    d=[[0,-1],[-1,0],[0,1],[1,0]]
    while 1:
        if(not(0<=cur[0]+d[idx][0]<f[0][0]+1 and 0<=cur[1]+d[idx][1]<C)):
            idx=(idx+1)%4
            
        nextY=cur[0]+d[idx][0]
        nextX=cur[1]+d[idx][1]
        if(A[nextY][nextX]>0):
            if(A[cur[0]][cur[1]]==-1):
                A[nextY][nextX]=0
                continue
            A[cur[0]][cur[1]]=A[nextY][nextX]
            A[nextY][nextX]=0

        cur[0]+=d[idx][0]
        cur[1]+=d[idx][1]
        

        if(f[0]==[cur[0],cur[1]]):
            break


    idx=0
    startY=f[1][0]
    startX=f[1][1]
    cur=[startY,startX]
    d=[[0,-1],[1,0],[0,1],[-1,0]]
    while 1:
        if(not(f[1][0]<=cur[0]+d[idx][0]<R and 0<=cur[1]+d[idx][1]<C)):
            idx=(idx+1)%4
        nextY=cur[0]+d[idx][0]
        nextX=cur[1]+d[idx][1]
        if(A[nextY][nextX]>0):
            if(A[cur[0]][cur[1]]==-1):
                A[nextY][nextX]=0
                continue
            A[cur[0]][cur[1]]=A[nextY][nextX]
            A[nextY][nextX]=0

        cur[0]+=d[idx][0]
        cur[1]+=d[idx][1]
        if(f[1]==[cur[0],cur[1]]):
            break
 
      
def countDusts(A:list)->int:
    cnt=2
    for y in range(R):
        for x in range(C):
            cnt+=A[y][x]
    return cnt   

for _ in range(T):
    spread(A)
    cycleAndFurify(A,fu)

print(countDusts(A))
    
    
    

    

