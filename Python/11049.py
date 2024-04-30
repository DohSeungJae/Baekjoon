import sys
input=sys.stdin.readline

N=int(input())
dp=[[0 if(i==j) else sys.maxsize for j in range(N)] for i in range(N)]
mat=[]

for _ in range(N):
    mat.append(list(map(int,input().split())))

for i in range(N-1):
    y,x=i,i+1
    dp[y][x]=mat[x-1][0]*mat[y+1][0]*mat[y+1][1]

for diagonal in range(2,N):
    for d in range(N-diagonal):
        i,j=d,d+diagonal
        for distance in range(diagonal):
            y,x=i+1+distance,i+distance
            dp[i][j]=min(dp[i][j],(dp[i][x]+dp[y][j]+(mat[i][0]*mat[y][0]*mat[j][1])))

print(dp[0][N-1])