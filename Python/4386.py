import sys
import heapq
input=sys.stdin.readline

n=int(input())

#노드 입력
nList=[]
for _ in range(n):
    nList.append(list(map(float,input().split()))) 

#완전 그래프 생성
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
for v in range(n):
    for u in range(n):
        if(v==u or v>u):
            continue
        cost=(((nList[u][0]-nList[v][0])**2)+((nList[u][1]-nList[v][1])**2))**0.5
        graph[v+1].append((cost,u+1))
        graph[u+1].append((cost,v+1))
      
#MST, 최소 비용 계산
ans=0
cnt=0
hq=[(0,1)]
while hq:
    if(cnt==n):
        break
    cost,cur=heapq.heappop(hq)
    if not visited[cur]:
        visited[cur]=1
        ans+=cost
        cnt+=1
        for next in graph[cur]:
            heapq.heappush(hq,next)
print("{:.2f}".format(ans))
