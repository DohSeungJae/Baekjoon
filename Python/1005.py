from collections import deque
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    dp=[0 for _ in range(N+1)]
    indegree=[0 for _ in range(N+1)]
    timeOf=[0]+list(map(int,input().split()))
    graph=[[] for _ in range(N+1)]
    
    for _ in range(K):
        X,Y=map(int,input().split())
        graph[X].append(Y)
        indegree[Y]+=1

    q=deque()
    for i in range(1,N+1):
        if(indegree[i]==0):
            q.append(i)
            dp[i]=timeOf[i]
            
    while q:
        cur=q.popleft()
        for next in graph[cur]:
            indegree[next]-=1
            dp[next]=max(dp[cur]+timeOf[next],dp[next])
            if(indegree[next]==0):
                q.append(next)
                
    W=int(input())
    print(dp[W])


            