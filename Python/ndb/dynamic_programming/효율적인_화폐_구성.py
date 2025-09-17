import sys
input=sys.stdin.readline

N,M=map(int,input().split())
coins=[]

for _ in range(N):
    coins.append(int(input()))

dp=[sys.maxsize]*(M+1)
dp[0]=0

for i in range(1,M+1):
    for j in range(N):
        if(coins[j]>i):
            continue
        if(dp[i-coins[j]]==sys.maxsize):
            continue
        dp[i]=min(dp[i],dp[i-coins[j]]+1)

ans=0
if(dp[M]==sys.maxsize):
    ans=-1
else:
    ans=dp[M]

print(ans)


            
    