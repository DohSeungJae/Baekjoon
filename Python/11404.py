import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

dist=[[sys.maxsize for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        if(y==x):
            dist[y][x]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    dist[a-1][b-1]=min(c,dist[a-1][b-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if(dist[i][k]+dist[k][j]<dist[i][j]):
                dist[i][j]=dist[i][k]+dist[k][j]


for row in dist:
    for i in row:
        if(i==sys.maxsize):
            print(0,end=" ")
        else:
            print(i,end=" ")
    print()
    


