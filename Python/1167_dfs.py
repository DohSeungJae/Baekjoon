import sys
input=sys.stdin.readline

V=int(input())
tree=[{} for _ in range(V+1)]

for _ in range(V):
    line=list(map(int,input().split()))
    p,cs=line[0],line[1:-1]
    for i in range(len(cs)//2):
        c,w=cs[(i*2)],cs[(2*i)+1]
        if(c in tree[p].keys()):
            tree[p][c]=max(tree[p][c],w)        
        else:
            tree[p][c]=w

        if(p in tree[c].keys()):
            tree[c][p]=max(tree[c][p],w)
        else:
            tree[c][p]=w
        
def dfs(curNode:int,curWeight:int)->None:
    for nextNode,nextWeight in tree[curNode].items():

        if(visited[nextNode]!=-1):
            continue
        visited[nextNode]=curWeight+nextWeight
        dfs(nextNode,curWeight+nextWeight)

visited=[-1]*(V+1)
visited[1]=0
dfs(1,0)

extermeLeafNode=visited.index(max(visited))
visited=[-1]*(V+1)
visited[extermeLeafNode]=0
dfs(extermeLeafNode,0)

print(max(visited))





