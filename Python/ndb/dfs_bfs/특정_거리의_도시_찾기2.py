from collections import deque
#import sys
#input=sys.stdin.readline
#sys 라이브러리 사용 시 Python3에서 정답처리, 쓰지 않으면 TLE
#Pypy3에서는 관계 없이 통과 

n,m,k,x=map(int,input().split())

dist=[-1]*(n+1) #방문하지 않은 경우 -1
dist[x]=0 #자신의 경우 0
edges=[[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    edges[s].append(e)

q=deque()
q.append(x)
while q:
    now=q.popleft()
    for nxt in edges[now]:
        if(dist[nxt]!=-1): #방문한 경우 제외
            continue
        dist[nxt]=dist[now]+1
        q.append(nxt)

cnt=0
for i in range(1,n+1):
    if(dist[i]==k):
        cnt+=1
        print(i)

if(cnt==0):
    print(-1)
