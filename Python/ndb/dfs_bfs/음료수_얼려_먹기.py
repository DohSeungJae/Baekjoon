import sys
input=sys.stdin.readline

dy=[1,-1,0,0]
dx=[0,0,1,-1]

N,M=map(int,input().split())

board=[]
for _ in range(N):
    board.append(list(map(int,input().strip())))

def dfs(y,x):
    board[y][x]=1
    
    for i in range(4):
        next_y=y+dy[i]
        next_x=x+dx[i]
        if(next_y>=N or next_y<0 or next_x>=M or next_x<0):
            continue
        if(board[next_y][next_x]==1): 
            continue 
        dfs(next_y,next_x)

cnt=0
for y in range(N):
    for x in range(M):
        if(board[y][x]==1):
            continue
        dfs(y,x)
        cnt+=1

print(cnt)
