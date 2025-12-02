from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def get_union(x,y,visited):
    if(visited[y][x]==1):
        return None
    q=deque([[x,y]])
    union=[[x,y]]
    visited[y][x]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(nx<0 or nx>=n or ny<0 or ny>=n):
                continue
            if(visited[ny][nx]==1):
                continue
            diff=abs(board[ny][nx]-board[y][x])
            if(l<=diff<=r):
                visited[ny][nx]=1
                q.append([nx,ny])
                union.append([nx,ny])

    if(len(union)==1):
        return None
    
    return union


n,l,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

day=0
while 1:
    unions=[]
    visited=[[0]*n for _ in range(n)] #0:미방문, 1:방문
    for y in range(n):
        for x in range(n):
            union=get_union(x,y,visited)
            if(union==None):
                continue
            unions.append(union)
    
    if(unions==[]):
        break

    for union in unions:
        total=0
        cnt=len(union)
        for x,y in union:
            total+=board[y][x]
        for x,y in union:
            board[y][x]=total//cnt
    
    day+=1

print(day)