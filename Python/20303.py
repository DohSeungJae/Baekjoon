import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

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

N,M,K=map(int,input().split())
candies=list(map(int,input().split()))
parent=[i for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    unionParent(parent,a,b)

bundle={}
for i in range(1,N+1):
    p=findParent(parent,i)
    if(p not in bundle.keys()):
        bundle[p]=[1,candies[i-1]]
    else:
        bundle[p][0]+=1
        bundle[p][1]+=candies[i-1]

bag=[[0,0]]
for b in bundle.values():
    bag.append(b)

dp=[[0]*(K+1) for _ in range(len(bag))]
for i in range(1,len(bag)):
    k=bag[i][0]
    c=bag[i][1]
    for j in range(1,K+1):
        if(j<=k):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-k]+c)

print(dp[-1][-1])
