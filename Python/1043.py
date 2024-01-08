import sys
input=sys.stdin.readline

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

N,M=map(int,input().split())
knower=list(map(int,input().split()))
parent=[i for i in range(N+1)]
ans=0

root=0
if(knower[0]>=1):
    unionParent(parent,root,knower[1])
    for i in range(1,knower[0]):
        unionParent(parent,knower[i],knower[i+1])

partyList=[]
for _ in range(M):
    party=list(map(int,input().split()))
    partyList.append(party)
    for i in range(1,party[0]):
        unionParent(parent,party[i],party[i+1])
    
if(knower[0]==0):
    print(M)
    exit(0)

for party in partyList:
    if(not findParent(parent,party[1])==root):
        ans+=1

print(ans)
