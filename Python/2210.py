import sys
inpuit=sys.stdin.readline
s=5
res=[]
board=[list(map(str,input().strip().split())) for _ in range(s)]


def bfs(x,y,num):
    if len(num)==6:
        if num not in res:
            res.append(num)
        return 

    aroundX=[1,-1,0,0]
    aroundY=[0,0,1,-1]
    for i in range(4):
        nx=x+aroundX[i]
        ny=y+aroundY[i]

        if(0<=nx<s and 0<=ny<s):
            bfs(nx,ny,num+board[ny][nx])


for y in range(s):
    for x in range(s):
        bfs(x,y,board[y][x])    

print(res)
print(len(res))
