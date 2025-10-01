from collections import deque
import sys
input=sys.stdin.readline

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
indegree=[0]*(v+1)

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if(indegree[i]==0):
            q.append(i)

    while q:
        now=q.popleft()
        result.append(now)
        for nxt in graph[now]:
            indegree[nxt]-=1
            if(indegree[nxt]==0):
                q.append(nxt)
    
    for i in result:
        print(i, end=" ")
    print()

topology_sort()


