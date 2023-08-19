import sys
input=sys.stdin.readline

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visitIdx=[]
aroundX=[-1,1,0,0]
aroundY=[0,0,-1,1]
res=0

def dfs(x,y,v,leng):
    global res
    if(leng==4):
        res=max(res,v)
        return 
    
    for i in range(4):
        nx=x+aroundX[i]
        ny=y+aroundY[i]
        if(0<=nx<m and 0<=ny<n and [nx,ny] not in visitIdx):
            visitIdx.append([nx,ny])
            dfs(nx,ny,v+board[ny][nx],leng+1)
            visitIdx.pop()

def exception(x,y):
    global res
    around=[]
    for i in range(4):
        nx=x+aroundX[i]
        ny=y+aroundY[i]
        if(0<=nx<m and 0<=ny<n):
            around.append(board[ny][nx])

    if(len(around)<3):
        return 

    elif(len(around)==4):
        around.remove(min(around))

    around.append(board[y][x])
    res=max(res,sum(around))

for y in range(n):
    for x in range(m):
        visitIdx.append([x,y])
        dfs(x,y,board[y][x],1)
        visitIdx.pop()
        exception(x,y)

print(res)