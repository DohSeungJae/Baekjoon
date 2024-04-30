import sys
input=sys.stdin.readline

N=int(input())
dp=[[0 if(i==j) else sys.maxsize for j in range(N)] for i in range(N)]
mat=[]

for _ in range(N):
    mat.append(list(map(int,input().split())))

#대각선 처리 2중 for문
for diagonal in range(1,N):
    for d in range(0,N-diagonal):
        i,j=d,d+diagonal
        dp[i][j]=min(dp[i][j-1]+mat[i][0]*mat[j][0]*mat[j][1],
                     dp[i+1][j]+mat[j][1]*mat[i][1]*mat[i][0])

print(dp[0][N-1])
