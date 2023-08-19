
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))


max_path=-1
visit=set()
nextX=[-1,1,0,0]
nextY=[0,0,-1,1]

def dfs(x,y,cnt):
    global max_path
    max_path=max(max_path,cnt)
    
    for i in range(4):
        nx=x+nextX[i]
        ny=y+nextY[i]

        if((0<=nx<m and 0<=ny<n) and graph[ny][nx] not in visit):
            visit.add(graph[ny][nx])
            dfs(nx,ny,cnt+1)
            visit.remove(graph[ny][nx])


visit.add(graph[0][0])      
dfs(0,0,1)
print(max_path)

