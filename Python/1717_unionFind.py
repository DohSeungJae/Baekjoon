import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def findParent1(parent,x):
    if(parent[x]!=x):
        parent[x]=findParent1(parent,parent[x])
    return parent[x]

def findParentCompressed(parent,x):
    if(parent[x]==x):
        return x
    parent[x]=findParentCompressed(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a=findParentCompressed(parent,a)
    b=findParentCompressed(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[i for i in range(n+1)]
for i in range(n+1):
    parent[i]=i

for _ in range(m):
    mode,a,b=map(int,input().split())
    if(mode==0):
        unionParent(parent,a,b)
    else:
        if(findParentCompressed(parent,a)==findParentCompressed(parent,b)):
            print("YES")
        else:
            print("NO")

    