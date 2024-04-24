import sys
input=sys.stdin.readline

N,M=map(int,input().split())
ms=[0]+list(map(int,input().split()))
cs=[0]+list(map(int,input().split()))

dp=[[0]*(sum(cs)+1) for _ in range(N+1)]
res=sys.maxsize

for i in range(1,N+1):
    for j in range(sum(cs)+1):
        m,c=ms[i],cs[i]
        if(j<c):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-c]+m)
        
        if(dp[i][j]>=M):
            res=min(res,j)
            
print(res)
