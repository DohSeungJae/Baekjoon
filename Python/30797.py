import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n,Q=map(int,input().split())
parent=[0]*(n+1)
selfReference=0

for i in range(n+1):
    parent[i]=i

def findParent(parent:list,x:int)->int:
    if(parent[x]!=x):
        parent[x]=findParent(parent,parent[x])
    return parent[x]

def unionParent(parent:list,a:int,b:int)->None:
    a=findParent(parent,a)
    b=findParent(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

edges=[]

totalCost=0
completedTime=0
for _ in range(Q):
    fr,to,co,tm=map(int,input().split())
    edges.append((co,tm,fr,to))

edges.sort(key=lambda x:(x[0],x[1]))

for i in range(Q):
    fr=edges[i][2]
    to=edges[i][3]
    if(findParent(parent,fr)!=findParent(parent,to)):
        unionParent(parent,fr,to)
        totalCost+=edges[i][0]
        completedTime=max(completedTime,edges[i][1])

for i in range(1,n+1):
    if(i==parent[i]):
        selfReference+=1

if(selfReference>1):
    print(-1)
    exit(0)

print(completedTime,totalCost)






    

