import sys
input=sys.stdin.readline

N=int(input())
costRgb=[list(map(int,input().split())) for _ in range(N)]
minCost=sys.maxsize

for i in range(3):
    dp=[[1001]*3 for _ in range(N)]
    dp[0][i]=costRgb[0][i]

    for j in range(1,N):
        dp[j][0]=costRgb[j][0]+min(dp[j-1][1],dp[j-1][2])
        dp[j][1]=costRgb[j][1]+min(dp[j-1][0],dp[j-1][2])
        dp[j][2]=costRgb[j][2]+min(dp[j-1][1],dp[j-1][0])
    dp[-1][i]=sys.maxsize
    minCost=min(minCost,min(dp[-1]))

print(minCost)
