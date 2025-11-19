from collections import deque

n,m,k,x=map(int,input().split())

dist=[300000+1]*(n+1) ### 
###범위 주석에 있는 코드를 사용할 경우 초기값은 -1

dist[x]=0
edge=[[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    edge[s].append(e)

visited=[0]*(n+1) ### 

q=deque()
q.append(x)
while q:
    now=q.popleft()
    for nxt in edge[now]:
        if(visited[nxt]==0):###
            dist[nxt]=min(dist[nxt],dist[now]+1) ###
            q.append(nxt) ###
            visited[nxt]=1 ###
        '''
        if(dist[nxt]==(-1)):
            dist[nxt]=dist[now]+1
            q.append(nxt)
        '''
        
cnt=0
for i in range(1,n+1):
    if(dist[i]==k):
        print(i)
        cnt+=1

if(cnt==0):
    print(-1)
