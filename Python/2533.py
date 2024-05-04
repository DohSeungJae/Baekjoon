import sys
input=sys.stdin.readline
N=int(input())
tree=[[] for _ in range(N+1)]
dp=[0]*(N+1)
visited=[0]*(N+1)
sys.setrecursionlimit(10**6)

for _ in range(N-1):
    u,v=map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(cur:int)->int:
    spreaded=1
    visited[cur]=1
    for next in tree[cur]:
        if(visited[next]):
            continue
        childSpreaded=dfs(next)
        spreaded=spreaded and childSpreaded
        dp[cur]+=dp[next]
    if(not tree[cur]): #이어진 노드가 없는 상태 
        return 0
    
    if(tree[cur] and not spreaded): #이어진 노드는 있지만 확산되지 않은 상태
        dp[cur]+=1
        return 1
    else: #이어진 노드가 있으며 확산된 상태 
        return 0
    
dfs(1)
print(dp[1])
#feedback 
#입력 u,v가 주어졌을 때, u가 부모, v가 자식이라고 명시된 적이 없음
#이런 경우 양방향 그래프를 사용해야함