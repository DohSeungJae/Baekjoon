from itertools import combinations

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def get_safe_area():
    safe_area=0
    board=[[0]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            board[y][x]=graph[y][x]

    for virus_x,virus_y in virus:
        dfs(board,virus_x,virus_y)
    
    for y in range(n):
        for x in range(m):
            if(board[y][x]==0):
                safe_area+=1
    
    return safe_area

def dfs(board,x,y): #바이러스 좌표    
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if(ny<0 or ny>=n or nx<0 or nx>=m):
            continue
        if(board[ny][nx]==1 or board[ny][nx]==2):
            continue
        board[ny][nx]=2
        dfs(board,nx,ny)

space=[] #빈 공간 [[x,y]] 형식
virus=[] #바이러스 위치 [[x,y]] 형식
graph=[]
n,m=map(int,input().split())
for y in range(n):
    line=list(map(int,input().split()))
    graph.append(line)
    for x in range(m):
        if(line[x]==0):
            space.append([x,y])
        if(line[x]==2):
            virus.append([x,y])

max_area=0
for add in combinations(space,3):
    for i in range(3):
        x,y=add[i]
        graph[y][x]=1

    safe_area=get_safe_area()
    max_area=max(max_area,safe_area)
    for i in range(3):
        x,y=add[i]
        graph[y][x]=0

print(max_area)
