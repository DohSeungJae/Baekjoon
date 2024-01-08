import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def findParent(parent,x):
    if(parent[x]!=x):
        parent[x]=findParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a=findParent(parent,a)
    b=findParent(parent,b)
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
        if(findParent(parent,a)==findParent(parent,b)):
            print("YES")
        else:
            print("NO")

    