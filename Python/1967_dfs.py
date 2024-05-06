import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

N=int(input())
tree=[[] for _ in range(N+1)]

for _ in range(N-1):
    p,c,w=map(int,input().split())
    tree[p].append((c,w))
    tree[c].append((p,w))

def dfs(curNode:int,curWeight:int)->None:
    for nextNode,nextWeight in tree[curNode]:
        if(visited[nextNode]!=-1):
            continue
        visited[nextNode]=curWeight+nextWeight
        dfs(nextNode,curWeight+nextWeight)

visited=[-1]*(N+1)
visited[1]=0
dfs(1,0)

extremeLeafNode=visited.index(max(visited))
visited=[-1]*(N+1)
visited[extremeLeafNode]=0
dfs(extremeLeafNode,0)

print(max(visited))
