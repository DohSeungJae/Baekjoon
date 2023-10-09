import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
visited=[0]*100001
cnt=[0]*100001

def bfs(v):
    q=deque()
    q.append(v)
    visited[v]=1
    cnt[v]=0

    while len(q)>0:
        v=q.popleft()
        if v==k:
            break

        for next in (v-1,v+1,2*v):
            if(next>100000 or next<0):
                continue
            if(visited[next]==0):
                if next==2*v:
                    cnt[next]=cnt[v]
                else:
                    cnt[next]=cnt[v]+1
                visited[next]=1
                q.append(next)

            else:
                if next==2*v:
                    cnt[next]=min(cnt[next],cnt[v])
                else:
                    cnt[next]=min(cnt[next],cnt[v]+1)

                q.append(next)
                



bfs(n)
print(cnt[k])


#숨바꼭질 3
