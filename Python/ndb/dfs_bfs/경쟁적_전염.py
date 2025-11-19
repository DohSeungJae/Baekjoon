from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,k=map(int,input().split())
board=[]
virus=[] #[[v,x,y] ...] 이때 n은 바이러스 번호

for y in range(n):
    line=list(map(int,input().split()))
    for x in range(n):
        if(line[x]!=0):
            v=line[x]
            virus.append([v,x,y])
    board.append(line)

virus.sort()
s,target_y,target_x=map(int,input().split())
target_y-=1
target_x-=1

q=deque()
for v,x,y in virus:
    q.append([v,x,y])

time=0
temp=deque()
while s>time:
    while temp:
        q.append(temp.popleft())
    while q:
        v,x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(nx>=n or nx<0 or ny>=n or ny<0):
                continue
            if(board[ny][nx]!=0):
                continue
            board[ny][nx]=v
            temp.append([v,nx,ny])
    time+=1

print(board[target_y][target_x])
