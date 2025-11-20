from collections import deque

n,k=map(int,input().split())
board=[]
virus=[] #[[v,x,y] ...]

for y in range(n):
    line=list(map(int,input().split()))
    for x in range(n):
        v=line[x]
        if(v!=0):
            virus.append([v,x,y])
    board.append(line)
virus.sort() ##!!!!!!

s,target_y,target_x=map(int,input().split())
target_y-=1
target_x-=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]

time=0
temp=deque()
q=deque()
for v,x,y in virus:
    q.append([v,x,y])
while s>time:
    while temp: 
        q.append(temp.popleft())
    while q:
        v,x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(nx<0 or nx>=n or ny<0 or ny>=n):
                continue
            if(board[ny][nx]!=0):
                continue
            board[ny][nx]=v
            temp.append([v,nx,ny])

    time+=1
    
print(board[target_y][target_x])

