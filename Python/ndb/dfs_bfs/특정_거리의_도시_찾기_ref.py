from collections import deque
import sys
input=sys.stdin.readline

n,m,k,x=map(int,input().split())

edges=[[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    edges[s].append(e)

dist=[1000000]*(n+1) #x에서 다른 곳으로 갈 수 있는 최단거리
visited=[0]*(n+1)
dist[x]=0
answer=[]
def bfs(start): #x가 들어감
    q=deque()
    q.append(start)

    while q:
        cur=q.popleft()
        visited[cur]=1
        for nxt in edges[cur]:
            cost=dist[cur]+1
            dist[nxt]=min(dist[nxt],cost)
            if(visited[nxt]==1):
                continue
            if(dist[nxt]==k and nxt not in answer):
                answer.append(nxt)
            q.append(nxt)

bfs(x)
#print(answer)
'''
exist=False
for i in range(1,n+1):
    if(i==x):
        continue
    if(dist[i]==k):
        print(i)
        exist=True

if(not exist):
    print(-1)
'''

if(len(answer)==0):
    print(-1)
    exit(0)
answer.sort()
for i in answer:
    print(i)


