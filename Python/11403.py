import sys
input=sys.stdin.readline

n=int(input())
dist=[]

for _ in range(n):
    dist.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if(dist[i][k]!=0 and dist[k][j]!=0):
                dist[i][j]=1

for i in dist:
    for j in i:
        print(j,end=" ")
    print()

#경로 찾기