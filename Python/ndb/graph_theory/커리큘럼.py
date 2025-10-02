import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
indegree=[0]*(n+1)
time=[0]*(n+1)
prev_time=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for i in range(1,n+1):
    line=list(map(int,input().split()))
    time[i]=line[0]
    for j in range(1,len(line)-1):
        graph[line[j]].append(i)
        indegree[i]+=1

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,n+1):
        if(indegree[i]==0):
            q.append(i)
        
    while q:
        now=q.popleft()
        result.append(now)
        for nxt in graph[now]:
            indegree[nxt]-=1
            prev_time[nxt]=max(prev_time[nxt],time[now]) #이 방식도 맞음
            if(indegree[nxt]==0):
                q.append(nxt)
                time[nxt]+=prev_time[nxt] #이 방식도 맞음

topology_sort()


for i in range(1,n+1):
    print(time[i])
    