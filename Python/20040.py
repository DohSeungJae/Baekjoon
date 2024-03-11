import sys
input=sys.stdin.readline

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
firstCycle=0
for t in range(1,m+1):
    a,b=map(int,input().split())
    if(firstCycle):
        continue
    if(findParent(parent,a)==findParent(parent,b)):
        firstCycle=t
    else:
        unionParent(parent,a,b)

print(firstCycle)
