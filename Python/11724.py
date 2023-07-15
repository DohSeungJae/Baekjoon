import sys
import queue
input=sys.stdin.readline

n,m=map(int,input().split())
matrix=[[0]*(n+1) for i in range(n+1)]

visit_list=[]
visited=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1

def bfs(matrix,v):
    visited=[]
    visited.append(v)

    q=queue.Queue()
    q.put(v)
    
    while not q.empty():
        v=q.get()
        for i in range(1,n+1):
            if(matrix[v][i]==1 and i not in visited):
                q.put(i)
                visited.append(i)


    return visited

cnt=0
visit=[]
for i in range(1,n+1):
    if not i in visit:
        cnt+=1
        visit+=bfs(matrix,i)


print(cnt)




    
