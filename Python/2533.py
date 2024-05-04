import sys
input=sys.stdin.readline

N=int(input())
tree=[[] for _ in range(N+1)]
dp=[0]*1000001

for _ in range(N-1):
    u,v=map(int,input().split())
    if(v in tree[u]):
        continue
    tree[u].append(v)

def dfs(cur:int)->int:
    spreaded=1
    for child in tree[cur]:
        childSpreaded=dfs(child)
        spreaded=spreaded and childSpreaded
        dp[cur]+=dp[child]
    if(not tree[cur]): #자식이 없는 상태 
        return 0
    
    if(tree[cur] and not spreaded): #자식이 있지만 확산되지 않은 상태
        dp[cur]+=1
        return 1
    else: #자식이 있고 확산된 상태
        return 0
    

dfs(1)
print(dp[1])
print(dp[:N])

#feedback 
#입력 u,v가 주어졌을 때, u가 부모, v가 자식이라고 명시된 적이 없음
#3
#2 1
#3 1
#위와 같이 입력이 주어질 경우, 루트를 1로 지정하게 된다면
#답이 0으로 나오게됨
#->
#트리를 단방향이 아닌 양방향으로 설정하고,
#visited 배열을 사용해 방문 체크를 하는 방식으로 진행해야함