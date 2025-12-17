from collections import deque

def get_union(board,visited,x,y):
    if(visited[y][x]==1): 
        return []
    union=[]  #[[x,y]...]
    union.append([x,y])
    q=deque() #[[x,y]...]
    q.append([x,y])
    visited[y][x]=1

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(ny>=n or ny<0 or nx>=n or nx<0):
                continue
            if(visited[ny][nx]==1):
                continue
            diff=abs(board[y][x]-board[ny][nx])
            if(l<=diff<=r):
                q.append([nx,ny])
                visited[ny][nx]=1
                union.append([nx,ny])

    if(len(union)==1): #이 조건문이 없으면
        return []   
        #인구 이동이 더 이상 발생하지 않는 경우(예를 들어 모든 값이 같은 경우)에서
        #무한 루프 발생 -> TLE
        #인구 이동이 발생하지 않음 -> 자기 자신을 연합에 넣음 -> if(unions==[]): break에서 걸리지 않고 계속 while문 실행됨

    return union

n,l,r=map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

day=0
while 1:
    visited=[[0]*n for _ in range(n)] #칸 별로 방문 여부를 체크해서 어떤 칸이 2개 이상의 union에 들어가지 않도록 처리 
    unions=[]
    for y in range(n):
        for x in range(n):
            union=get_union(board,visited,x,y)
            if(union==[]):
                continue
            unions.append(union)

    if(unions==[]):
        break 

    for union in unions:
        cnt=len(union)
        total=0
        for x,y in union:
            total+=board[y][x]
        for x,y in union:
            board[y][x]=total//cnt

    day+=1

print(day)
