import sys
input=sys.stdin.readline

MAX=(15)+1
n,m,r=map(int,input().split())

itemList=list(map(int,input().split()))
maxItems=0
dist=[[MAX for _ in range(n)] for _ in range(n)]

for _ in range(r):
    a,b,l=map(int,input().split())
    dist[a-1][b-1]=min(l,dist[a-1][b-1])
    dist[b-1][a-1]=min(l,dist[b-1][a-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if(dist[i][k]+dist[k][j]<dist[i][j]):
                dist[i][j]=dist[i][k]+dist[k][j]

for i in range(n):
    temp=0
    for j in range(n):
        if(dist[i][j]<=m or i==j):
            temp+=itemList[j]
    maxItems=max(temp,maxItems)
    
print(maxItems)



