import sys
import queue
input=sys.stdin.readline


n=int(input())
matrix=[[0]*(n+1) for i in range(n+1)]
m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1


visited=[0]*(n+1)

start=1
def dfs(v,matrix):
    visited[v]=1

    for next in range(1,n+1):
        if(visited[next]==0 and matrix[v][next]==1):
            dfs(next,matrix)

def bfs(v,matrix):
    q=queue.Queue()
    q.put(v)

    while not q.empty():
        v=q.get()

        for next in range(1,n+1):
            if visited[next]==0 and matrix[v][next]==1:
                q.put(next)
                visited[next]=1


    

bfs(start,matrix)
print(sum(visited)-1)

