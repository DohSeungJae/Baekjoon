import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dist=[[0]*(n+1) for i in range(n+1)]
for y in range(1,n+1):
    for x in range(1,n+1):
        if(y==x):
            dist[y][x]=0
        else:
            dist[y][x]=sys.maxsize

for _ in range(m):
    a,b=map(int,input().split())
    dist[a][b]=1
    dist[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(dist[i][k]+dist[k][j]<dist[i][j]):
                dist[i][j]=dist[i][k]+dist[k][j]


mmin=sys.maxsize
min_idx=0
for i in range(1,n+1):
    cur=sum(dist[i])
    if(cur<mmin):
        min_idx=i
        mmin=cur

print(min_idx)


#케빈 베이컨의 6단계 법칙