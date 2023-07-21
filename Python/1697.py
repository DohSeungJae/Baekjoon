import sys
import queue
input=sys.stdin.readline

n,k=map(int,input().split())

visited=[0]*100001

def bfs(v):
    q=queue.Queue()
    q.put(v)
    visited[v]=0
    
    while not q.empty():
        v=q.get()
        if v==k:
            break

        for next in (v-1,v+1,2*v):
            if(next>100000 or next<0):
                continue
            if(visited[next]==0):
                visited[next]+=visited[v]+1
                q.put(next)

bfs(n)
print(visited[k])

