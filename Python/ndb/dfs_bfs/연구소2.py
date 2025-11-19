from itertools import combinations

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def get_safe_area(board,virus):
    copy=[[0]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            copy[y][x]=board[y][x]
            
    for x,y in virus:
        dfs(x,y,copy)

    safe_area=0 
    for y in range(n):
        for x in range(m):
            if(copy[y][x]==0):
                safe_area+=1
    
    return safe_area

def dfs(x,y,graph):
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if(nx>=m or nx<0 or ny>=n or ny<0):
            continue 
        if(graph[ny][nx]==1 or graph[ny][nx]==2):
            continue
        
        graph[ny][nx]=2
        dfs(nx,ny,graph)
    
n,m=map(int,input().split())

blank=[] #[[x,y] ... ]
virus=[] #[[x,y] ... ]
board=[]
for y in range(n):
    line=list(map(int,input().split()))
    for x in range(m):
        if(line[x]==0):
            blank.append([x,y])
        elif(line[x]==2):
            virus.append([x,y])
    board.append(line)

max_area=0
for build in combinations(blank,3):
    for i in range(3):
        x,y=build[i]
        board[y][x]=1
    
    safe_area=get_safe_area(board,virus)
    max_area=max(max_area,safe_area)

    for i in range(3):
        x,y=build[i]
        board[y][x]=0

print(max_area)

