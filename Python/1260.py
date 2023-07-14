import sys
import queue
   
input=sys.stdin.readline


n,m,v=map(int,input().split())
matrix=[[0]*(n+1) for i in range(n+1)]

visited_dfs=[0]*(n+1)
visited_bfs=[0]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1


def dfs(matrix,v):
    print(v,end=" ")
    visited_dfs[v]=1

    for next in range(1,n+1):
        if matrix[v][next]==1 and visited_dfs[next]==0:
            dfs(matrix,next)
    



def bfs(matrix,v):
    visited_bfs[v]=1
    q=queue.Queue()
    q.put(v)
    
    while not q.empty():
        v=q.get()
        print(v,end=" ")
        for i in range(1,n+1):
            if(matrix[v][i]==1 and visited_bfs[i]==0):
                q.put(i)
                visited_bfs[i]=1

    print()



    


print(matrix)
dfs(matrix,v)
print()
bfs(matrix,v)




