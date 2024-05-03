import sys
input=sys.stdin.readline

def findParent(parent:list[list[int]],x:int)->int:
    if(parent[x]!=x):
        parent[x]=findParent(parent,parent[x])
    return parent[x]

def unionParent(parent:list[list[int]],a:int,b:int)->None:
    a=findParent(parent,a)
    b=findParent(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

def dfs(y:int,x:int):
    visited[y][x]=1
    dy,dx=directionOf[board[y][x]]
    nextY,nextX=y+dy,x+dx
    
    unionParent(parent,x+(y*M),nextX+(nextY*M))
    if(visited[nextY][nextX]):
        return
    dfs(nextY,nextX)

N,M=map(int,input().split())
board=[]
visited=[[0 for _ in range(M)] for _ in range(N)]
parent=[i for i in range(M*N)]
directionOf={"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
for _ in range(N):
    board.append([i for i in input().strip()])

for y in range(N):
    for x in range(M):
        idx=x+(y*M)
        if(visited[y][x]):
            continue
        dfs(y,x)

isRoot={}
rootCnt=0
for i in range(len(parent)):
    if(i==parent[i] and i not in isRoot.keys()):
        isRoot[i]=1
        rootCnt+=1

print(rootCnt)


